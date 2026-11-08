# Independent mathematical audit

## correctness

PASS

Derived clique update from s=c+p and degree a+b-1: if total even and s=(a+b)/2 the entire clique complements, otherwise becomes constant; independent word becomes 0,I,1 according to 2c<a,=a,>a. Thus any state reaches a corner or two-cycle by time 2, and a>b corners collapse in one more step. Enumerating central line 1<=p<=b-1 excluding c=a/2 yields exact three-round phase iff a>b, even a+b, b>=3; Vandermonde subtraction gives E3=C(a+b,r)-2C(a,r)-1_{a even} C(a,a/2)C(b,b/2). Recurrent corners, central ties, and endpoints give R=2+2*1_{a<=b}+2*1_{a>b,even total}C(a,r)+1_{a,b even}C(a,a/2)C(b,b/2). Independent exhaustive direct graph updates for every a,b in [1,6] with a+b<=9 confirmed each relevant formula. Central binomial asymptotics give P(T=3)~sqrt(2/(pi(a+b))) as b grows, a>b. The finite check is corroboration, not the proof.

## originality

PASS

Goles–Olivos 1980 general symmetric threshold eventual periods <=2; Kaaser–Mallmann-Trenn–Natale 2015/2016 analyzes majority voting time and module contraction, but not this three-round asymmetric complete split partition/census. Earlier balanced a=b two-round case does not imply a>b three-round regime.

## value

PASS

Complete classification of a natural two-module majority graph family, with exact transient-layer counts, recurrent-cycle census, and rare maximal-transient asymptotics; finer than generic period-two theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
