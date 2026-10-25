// Exact covering-set check in PG(2,5): every cover using <=8 lines contains a full pencil.
#include <array>
#include <vector>
#include <cstdint>
#include <iostream>
using namespace std;
int main(){
 vector<array<int,3>> P; for(int y=0;y<5;y++)for(int z=0;z<5;z++)P.push_back({1,y,z});for(int z=0;z<5;z++)P.push_back({0,1,z});P.push_back({0,0,1});
 uint32_t cover[31]={}, pencil[31]={};
 for(int l=0;l<31;l++)for(int p=0;p<31;p++)if((P[l][0]*P[p][0]+P[l][1]*P[p][1]+P[l][2]*P[p][2])%5==0){cover[l]|=(1u<<p);pencil[p]|=(1u<<l);}
 long long total=0,covering=0,notpencil=0;uint32_t ALL=0x7fffffff;
 // Gosper's hack enumerates all 8-sets of 31 lines. Smaller sets extend to 8-sets.
 for(uint32_t s=(1u<<8)-1;s<=(ALL^0u);){
    total++;uint32_t points=0;for(int i=0;i<31;i++)if(s&(1u<<i))points|=cover[i];
    if(points==ALL){covering++;bool haspencil=false;for(int p=0;p<31;p++)if((s&pencil[p])==pencil[p])haspencil=true;if(!haspencil)notpencil++;}
    uint32_t c=s&-s,r=s+c;if(!r||r>=0x80000000u)break;s=(((r^s)>>2)/c)|r;
 }
 cout<<"eight_line_sets "<<total<<" covering "<<covering<<" covering_without_pencil "<<notpencil<<"\n";
 return (notpencil!=0);
}
