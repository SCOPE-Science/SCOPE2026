#include <algorithm>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// Independent bit-by-bit implementation; every automaton state is mapped separately.
int apply(int x,int k,int op){
    int y=0;
    for(int i=0;i<k;i++) if((x>>i)&1){
        int dest = (op==0) ? ((i+1)%k) : ((i==k-1)?0:i);
        y|=1<<dest;
    }
    return y;
}
int main(){
    ofstream out("table_cpp.csv");
    out << "m,n,length,word,visited_before_goal\n";
    int count=0;
    for(int n=3;n<=11;n++) for(int m=2;m<n;m++){
        const int lower=(1<<m)-1, upper=(1<<n)-1;
        const int bits=m+n, maxst=1<<bits;
        int start=lower | (upper<<m);
        vector<int> parent(maxst,-1);
        vector<char> letter(maxst,0);
        vector<int> queue;queue.reserve(maxst);
        queue.push_back(start);parent[start]=start;
        int goal=-1;
        for(size_t qi=0;qi<queue.size();qi++){
            int cur=queue[qi];
            int x=cur&lower, y=cur>>m;
            if(__builtin_popcount((unsigned)x)==1 && __builtin_popcount((unsigned)y)==1){goal=cur;break;}
            for(int op=0;op<2;op++){
                int nx=apply(x,m,op),ny=apply(y,n,op);
                int dest=nx|(ny<<m);
                if(parent[dest]==-1){parent[dest]=cur;letter[dest]=op==0?'a':'b';queue.push_back(dest);}
            }
        }
        if(goal==-1) return 2;
        string w;
        for(int z=goal;z!=start;z=parent[z])w+=letter[z];
        reverse(w.begin(),w.end());
        for(int k:{m,n}){
            int state=(1<<k)-1;
            for(char c:w)state=apply(state,k,c=='a'?0:1);
            assert(__builtin_popcount((unsigned)state)==1);
        }
        out<<m<<","<<n<<","<<w.size()<<","<<w<<","<<queue.size()<<"\n";
        count++;
    }
    cout<<"VERIFY_OK CPP "<<count<<"\n";
}
