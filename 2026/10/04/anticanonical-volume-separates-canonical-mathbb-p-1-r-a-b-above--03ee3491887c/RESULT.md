# Anticanonical volume separates canonical \(\mathbb P(1^r,a,b)\) above dimension three
## Finding
For every integer \(r\ge 2\), consider
\[
X_{r,a,b}=\mathbb P(1^r,a,b),\qquad 1\le a\le b,
\]
with at worst canonical singularities. Put
\[
V_r(a,b)=(-K_{X_{r,a,b}})^{r+1}.
\]
Then \(V_r\) is injective on the canonical family for every \(r\ge3\). In the threefold case \(r=2\), exactly two collisions occur:
\[
V_2(1,1)=V_2(2,4)=64,
\qquad
V_2(1,3)=V_2(4,6)=72.
\]
There are no other equal-volume non-isomorphic members of this family.

## Assumptions and scope
The ground field is \(\mathbb C\). We use the standard well-formed weighted projective space with \(r\) weight-one coordinates and two additional weights \(a\le b\); its dimension is \(r+1\). Canonical means at worst canonical singularities in the usual birational-geometric sense.

Writing \(d=b-a\), the canonical members of this two-heavy-weight family are exactly
\[
0\le d\le r,
\qquad
1\le a\le r+d,
\qquad
b=a+d.
\]
This parametrization is rederived below from the cyclic quotient charts rather than assumed from a finite classification.

## Proof
On the chart of the coordinate of weight \(b\), the local cyclic quotient has weights \((1^r,a)\) modulo \(b\). For the first nontrivial element its age is
\[
\frac{r+a}b=\frac{r+a}{a+d},
\]
so canonicity forces \(d\le r\). On the chart of weight \(a\), if \(d<a\), the first element has age \((r+d)/a\), hence \(a\le r+d\); if \(d\ge a\), that inequality is automatic because \(d\le r\).

Conversely assume \(d\le r\) and \(a\le r+d\). On the \(b\)-chart, for \(1\le k<b\), the age numerator is
\[
rk+(ak\bmod b)=rk+((-dk)\bmod b).
\]
If \(b\nmid dk\), this is
\[
rk+b-(dk\bmod b)\ge b+(r-d)k\ge b.
\]
If \(b\mid dk\), then either \(d=0\), when \(b=a\le r\), or \(dk\ge b\); in both cases \(rk\ge b\). Thus every nonidentity element has age at least one. On the \(a\)-chart, the age numerator is \(rk+(dk\bmod a)\). If \(a\le r\) this is at least \(a\). If \(a>r\), then necessarily \(0<d<a\); writing \(q=\lfloor dk/a\rfloor\le k-1\), the numerator is
\[
(r+d)k-qa\ge a+k(r+d-a)\ge a.
\]
Hence the stated triangular parametrization is exact.

For weighted projective space,
\[
-K_X\sim (r+a+b)H,
\qquad
H^{r+1}=\frac1{ab},
\]
so
\[
V_r(a,b)=\frac{(r+a+b)^{r+1}}{ab}.
\]
The canonical inequalities imply \(a\le2r\), \(b\le3r\), and therefore \(ab\le6r^2\).

Suppose two canonical pairs have the same volume. Set
\[
S_1=r+a+b,
\quad
S_2=r+c+e,
\quad
P_1=ab,
\quad
P_2=ce,
\quad
n=r+1.
\]
Writing \(S_1=gu\), \(S_2=gv\) with \(\gcd(u,v)=1\), equality of volumes gives
\[
u^nP_2=v^nP_1.
\]
Thus \(u^n\mid P_1\) and \(v^n\mid P_2\). If \(S_1\ne S_2\), at least one of \(u,v\) is at least two, so
\[
2^{r+1}\le6r^2.
\]
But \(2^9>6\cdot8^2\), and the strict inequality \(2^{r+1}>6r^2\) propagates for all \(r\ge8\). Hence \(S_1=S_2\) for \(r\ge8\). Equal volume then gives \(P_1=P_2\), and the unordered positive pair is determined by its sum \(a+b=S_1-r\) and product \(ab=P_1\). Since the weights are ordered, \((a,b)=(c,e)\).

The remaining cases \(3\le r\le7\) are a finite exact check over the triangular canonical domain; no collisions occur. For \(r=2\), the same exact check gives precisely the two displayed collisions.

## Verification
The accompanying script `verify_volume_collisions.py` uses exact rational arithmetic. It independently checks the cyclic-quotient age criterion against the triangular parametrization for \(2\le r\le40\), verifies the two \(r=2\) collision classes, verifies collision-freeness for every \(3\le r\le200\), and checks the elementary exponential bound used for the infinite tail. Running it prints `VERIFY_OK`.

The computation is a regression check, not the infinite proof: the argument above proves injectivity for every \(r\ge8\), while only \(3\le r\le7\) require finite exhaustion.

## Relationship to prior work
Kasprzyk gives general fractional-part criteria for canonical weighted projective spaces and classifications in fixed dimensions. Those results supply the standard canonical framework but do not state the all-dimensional injectivity of anticanonical volume on this two-heavy-weight family. Coates--Gonshaw--Kasprzyk--Nabijou study mutations of fake weighted projective spaces and degree-extremal examples; their mutation formulas make anticanonical degree a natural invariant to examine, but do not give this collision classification. DeVleming records the threefold volume equation and discusses \(\mathbb P(1,1,2,4)\) in a deformation setting; this confirms that one exceptional collision sits in a well-studied geometric locus, without implying the all-dimensional rigidity statement proved here.

The result is therefore a rigidity statement for a central Fano invariant: from dimension four onward, within this natural canonical family, the anticanonical volume alone recovers both non-unit weights.

## Limitations
The theorem is restricted to weighted projective spaces with exactly two weights different from one. It does not claim volume injectivity for arbitrary canonical weighted projective spaces, fake weighted projective spaces, or general toric Fano varieties. It also does not classify deformation or mutation equivalence; equal anticanonical volume is only a necessary numerical coincidence for such relations.

## References
1. A. M. Kasprzyk, *Classifying terminal weighted projective space*, arXiv:1304.3029 (2013), especially Proposition 2.5 and the surrounding canonical-weight criteria.
2. T. Coates, S. Gonshaw, A. M. Kasprzyk, N. Nabijou, *Mutations of Fake Weighted Projective Spaces*, arXiv:1312.0921 (2013; revised 2014).
3. K. DeVleming, *Moduli of surfaces in \(\mathbb P^3\)*, Compositio Mathematica 158 (2022), 1329--1374, DOI: 10.1112/S0010437X22007552.
