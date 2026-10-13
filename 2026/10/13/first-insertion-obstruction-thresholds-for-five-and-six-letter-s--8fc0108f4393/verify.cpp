#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>

using std::string;
using std::vector;

struct Census {
  int alphabet;
  int limit;
  std::array<int, 20> word{};
  vector<uint64_t> total, blocked;
  vector<string> extremals;

  Census(int q, int n): alphabet(q), limit(n), total(n+1), blocked(n+1) {}

  int indexed(int j, int gap) const {
    return j < gap ? word[j] : j == gap ? -1 : word[j-1];
  }

  bool all_insertions_square(int n, int gap) const {
    const int len=n+1;
    int forbidden=0;
    const int full=(1<<alphabet)-1;
    if(gap>0) forbidden |= 1<<word[gap-1];
    if(gap<n) forbidden |= 1<<word[gap];
    for(int half=2;half*2<=len;half++) {
      const int first=std::max(0,gap-2*half+1);
      for(int start=first;start<=gap && start+2*half<=len;start++) {
        bool fits=true;
        for(int j=0;j<half;j++) {
          const int a=indexed(start+j,gap);
          const int b=indexed(start+j+half,gap);
          if(a!=-1 && b!=-1 && a!=b) {fits=false;break;}
        }
        if(fits) {
          const int partner=gap<start+half ? gap+half : gap-half;
          forbidden |= 1<<indexed(partner,gap);
        }
      }
    }
    return forbidden==full;
  }

  bool squarefree_after_append(int n) const {
    for(int half=1;2*half<=n;half++) {
      bool square=true;
      for(int i=0;i<half;i++)
        if(word[n-1-i]!=word[n-1-half-i]) {square=false;break;}
      if(square) return false;
    }
    return true;
  }

  void visit(int n,int used) {
    total[n]++;
    if(used==alphabet) {
      for(int gap=0;gap<=n;gap++) if(all_insertions_square(n,gap)) {
        blocked[n]++;
        if(n==limit) {
          string s;
          for(int i=0;i<n;i++) s+=char('0'+word[i]);
          extremals.push_back(s);
        }
        break;
      }
    }
    if(n==limit)return;
    for(int c=0;c<=used && c<alphabet;c++) {
      word[n]=c;
      if(squarefree_after_append(n+1)) visit(n+1,std::max(used,c+1));
    }
  }
};

int main() {
  constexpr int qvalues[]={2,3,4,5,6};
  constexpr int smallest[]={2,4,6,10,14};
  constexpr uint64_t last_census[]={1,3,29,6936,6480694};
  constexpr uint64_t last_blocked[]={1,2,1,2,1};
  const vector<vector<string>> representatives={
    {"01"},{"0102","0121"},{"010232"},
    {"0102010343","0102324232"},{"01020103435343"}
  };
  for(int t=0;t<5;t++) {
    Census c(qvalues[t],smallest[t]);
    c.word[0]=0;c.visit(1,1);
    for(int n=1;n<c.limit;n++) assert(c.blocked[n]==0);
    assert(c.total[c.limit]==last_census[t]);
    assert(c.blocked[c.limit]==last_blocked[t]);
    assert(c.extremals==representatives[t]);
    std::printf("q=%d minimum=%d canonical_words=%llu terminal_census=%llu representatives=",
                c.alphabet,c.limit,(unsigned long long)c.blocked[c.limit],
                (unsigned long long)c.total[c.limit]);
    for(size_t i=0;i<c.extremals.size();i++)
      std::printf("%s%s",i?",":"",c.extremals[i].c_str());
    std::puts("");
  }
  std::puts("VERIFY_OK first_nonbifurcate_lengths_2_through_6");
}
