LoadPackage("ctbllib");;
orders:=[];; H:=fail;;
for label in ["L3(8)","L3(8).3","L3(8).6"] do
 t:=CharacterTable(label);;irr:=Irr(t);;names:=ClassNames(t);;orders:=OrdersClassRepresentatives(t);;centr:=SizesCentralizers(t);;
 for ai in Filtered([1..Length(orders)],i->orders[i]=2) do
  for bi in Filtered([1..Length(orders)],i->orders[i]=3) do
   for ci in Filtered([1..Length(orders)],i->orders[i]=7) do
    f:=Sum(irr,ch->ch[ai]*ch[bi]*ComplexConjugate(ch[ci])/ch[1]);;
    cmc:=Size(t)*f/(centr[ai]*centr[bi]);;
    Assert(0,cmc=ClassMultiplicationCoefficient(t,ai,bi,ci));;
    expect:=0;;en:=0;;
    if names[ai]="2a" and names[bi]="3a" then
     if label="L3(8)" and names[ci] in ["7g","7h"] then expect:=49;en:=1;
     elif label="L3(8)" and names[ci] in ["7i","7j","7k"] then expect:=105;en:=15/7;
     elif label="L3(8).3" and names[ci] in ["7c","7d"] then expect:=49;en:=1/3;
     elif label="L3(8).3" and names[ci]="7e" then expect:=105;en:=15/7;
     elif label="L3(8).6" and names[ci]="7b" then expect:=49;en:=1/3;
     elif label="L3(8).6" and names[ci]="7c" then expect:=105;en:=15/14;
     fi;
    fi;
    Print("CHECK raw_sum=",f," actual_CMC=",cmc," expected_CMC=",expect,"\n");
    Assert(0,cmc=expect and cmc/centr[ci]=en);
    Print("FROBENIUS ",label," ",names[ai]," ",names[bi]," ",names[ci]," normalized=",cmc/centr[ci]," CMC=",cmc,"\n");
   od;
  od;
 od;
od;
Print("ALL_THREE_CHARACTER_TABLES_OK\n");
Read("artifacts/L38G1-p73bB0.g1");;
a:=bin1;;
Read("artifacts/L38G1-p73bB0.g2");;
b:=bin1;; G:=Group(a,b);;
Assert(0,Order(a)=2 and Order(b)=3 and Order(a*b)=21 and Size(G)=16482816);
wordgroup:=function(file)
 local r,line,s,i,j,k;
 r:=[a,b];
 for line in SplitString(StringFile(file),"\n") do
  s:=SplitString(line," \t\r");
  if Length(s)>0 and not s[1] in ["echo","oup"] then
   if s[1]="mu" then i:=Int(s[2]);j:=Int(s[3]);k:=Int(s[4]);r[k]:=r[i]*r[j];
   elif s[1]="pwr" then i:=Int(s[2]);j:=Int(s[3]);k:=Int(s[4]);r[k]:=r[j]^i;
   elif s[1]="cj" then i:=Int(s[2]);j:=Int(s[3]);k:=Int(s[4]);r[k]:=r[i]^r[j];
   elif s[1]="cjr" then i:=Int(s[2]);j:=Int(s[3]);r[i]:=r[i]^r[j];
   else Error("unknown word opcode");fi;
  fi;
 od;
 return Group(r{[1,2]});
end;;
M1:=wordgroup("artifacts/L38G1-max1W1");; M2:=wordgroup("artifacts/L38G1-max2W1");; M5:=wordgroup("artifacts/L38G1-max5W1");;
Assert(0,Size(M1)=225792 and Size(M2)=225792 and Size(M5)=168);
P1:=List(RightTransversal(G,M1),t->M1^t);; P2:=List(RightTransversal(G,M2),t->M2^t);;
Assert(0,Length(P1)=73 and Length(P2)=73);
classes:=ConjugacyClasses(G);; invol:=Filtered(classes,c->Order(Representative(c))=2);;
Assert(0,Length(invol)=1);; xs:=AsList(invol[1]);; Assert(0,Length(xs)=4599);
sevens:=Filtered(classes,c->Order(Representative(c))=7);; Assert(0,Length(sevens)=11);
counts:=[];;
for c in sevens do
 z:=Representative(c);; pairs:=[];; n1:=0;;n2:=0;;nunion:=0;;n5:=0;;
 for x in xs do
  y:=x*z;
  if Order(y)=3 then
   H:=Group(x,y);; sz:=Size(H);; Add(pairs,sz);
   if sz=168 then
    Assert(0,IsConjugate(G,H,M5)); n5:=n5+1;
   elif sz=504 then
    Assert(0,IsomorphismGroups(H,PSL(2,8))<>fail);
    h1:=ForAny(P1,P->IsSubgroup(P,H)); h2:=ForAny(P2,P->IsSubgroup(P,H));
    if h1 then n1:=n1+1;fi; if h2 then n2:=n2+1;fi;
    if h1 or h2 then nunion:=nunion+1;fi;
   else Error("unexpected generated subgroup order");fi;
  fi;
 od;
 if Length(pairs)=49 then Assert(0,Set(pairs)=[168] and n5=49);
 elif Length(pairs)=105 then Assert(0,Set(pairs)=[504] and n1=56 and n2=56 and nunion=105);
 else Assert(0,Length(pairs)=0);fi;
 Add(counts,Length(pairs));
 Print("SEVEN_CLASS size=",Size(c)," pairs=",Length(pairs)," subgroup_orders=",Set(pairs)," M5=",n5," M1=",n1," M2=",n2," union=",nunion,"\n");
od;
Assert(0,SortedList(counts)=[0,0,0,0,0,0,49,49,105,105,105]);
Print("COMPLETE_SIMPLE_GROUP_SCAN_OK\n");
Read("artifacts/L38d3G1-p73bB0.g1");; a:=bin1;;
Read("artifacts/L38d3G1-p73bB0.g2");; b:=bin1;; E3:=Group(a,b);;
Assert(0,Order(a)=2 and Order(b)=12 and Order(a*b)=21 and Size(E3)=49448448);
N:=wordgroup("artifacts/L38d3G1-max1W1");;
Assert(0,Size(N)=16482816 and IsNormal(E3,N) and Index(E3,N)=3);
Print("INDEX_THREE_NORMAL_SOCLE_OK\n");
Read("artifacts/L38d6G1-p657B0.g1");; a:=bin1;;
Read("artifacts/L38d6G1-p657B0.g2");; b:=bin1;; E6:=Group(a,b);;
Assert(0,Order(a)=2 and Order(b)=18 and Order(a*b)=24 and Size(E6)=98896896);
N3:=wordgroup("artifacts/L38d6G1-max1W1");;
Assert(0,Size(N3)=49448448 and IsNormal(E6,N3) and Index(E6,N3)=2);
Print("INDEX_TWO_NORMAL_EXTENSION_OK\n");
Print("COMPLETE_ALL_GROUP_REPLAY_OK\n");
QUIT;
