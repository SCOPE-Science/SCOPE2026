# Sharp Ehrhart-positivity cutoff for joins of two lattice polygons

## Finding

Let \(P,Q\subset\mathbb R^2\) be full-dimensional lattice polygons, and let their **standard lattice join** be
\[
J=P*Q=\operatorname{conv}\bigl(\{(x,0,0):x\in P\}\cup\{(0,y,1):y\in Q\}\bigr)\subset\mathbb R^5.
\]
Write \(B_P,B_Q\) for the numbers of boundary lattice points, \(I_P,I_Q\) for interior lattice points, and put
\[
a=B_P+I_P-3,\quad b=I_P,\qquad c=B_Q+I_Q-3,\quad d=I_Q.
\]
In particular, \(a\ge b\ge0\) and \(c\ge d\ge0\). Define the following integral expressions:
\[
\begin{aligned}
U(a,b,c,d)&=137+12(a+c)-3ac+2ad+2bc-3bd-3b-3d,\\
V(a,b,c,d)&=45+10(a+c)-ac+bd-b-d.
\end{aligned}
\]
**All-parameter sign criterion.** The ordinary Ehrhart polynomial of \(J\) is coefficientwise nonnegative if and only if \(U\ge0\) and \(V\ge0\), and has all its coefficients strictly positive if and only if both inequalities are strict. The only coefficients that can be nonpositive are the coefficients of \(n\) and \(n^2\), equal respectively to \(U/60\) and \(V/24\).

**Sharp normalized-volume cutoff.** Let \(N=2\operatorname{area}(P)\) and \(M=2\operatorname{area}(Q)\); the normalized five-dimensional volume of the join is \(NM\). If \(NM<168\), **every Ehrhart coefficient of \(J\) is strictly positive**. At \(NM=168\), there is exactly one nonpositive Ehrhart-data type up to interchanging the factors: \((N,M,I_P,I_Q)=(12,14,0,0)\). It has a negative linear coefficient. The explicit empty lattice triangles
\[
P=\operatorname{conv}\{(0,0),(12,0),(0,1)\},\qquad
Q=\operatorname{conv}\{(0,0),(14,0),(0,1)\}
\]
attain the cutoff and satisfy
\[
[n]L_J(n)=-\frac1{15},\qquad[n^2]L_J(n)=\frac{71}{12}.
\]
Here \([n^j]\) extracts the coefficient of the indicated monomial. The uniqueness assertion concerns **Ehrhart data**, not uniqueness of a polygon up to lattice equivalence or any claim about arbitrary five-dimensional polytopes.

The two potential nonpositive coefficients are genuinely independent: the above example has negative linear but positive quadratic coefficient, whereas the join of the first triangle \(P\) with
\[
Q'=\operatorname{conv}\{(0,0),(1,0),(2,157)\}
\]
has a positive linear coefficient \(113/60\) and a negative quadratic coefficient \(-1/24\), with every other coefficient strictly positive.

## Assumptions and scope

All polygons are full-dimensional in their respective standard rank-two integer lattices. The join is the **height-one standard lattice join** in the product lattice \(\mathbb Z^5\), not an arbitrary lattice realization of a combinatorially equivalent join. Area is Euclidean coordinate area; normalized area is twice this area. Ehrhart positivity means coefficientwise nonnegativity in the ordinary monomial basis, distinct from magic-basis positivity. There is no claim of a minimal volume for other classes of five-dimensional polytopes, and no claim that arbitrary combinatorial joins have the same lattice-point series.

## Proof

**1. Pick data and the Ehrhart series.** For each lattice polygon, Pick's theorem and the usual Ehrhart numerator give
\[
h_P^*(z)=1+az+bz^2,\qquad h_Q^*(z)=1+cz+dz^2,
\]
where \(a-b=B_P-3\ge0\) and \(c-d=B_Q-3\ge0\). The standard-join Ehrhart generating-function identity yields
\[
\sum_{n\ge0}L_J(n)z^n
=\frac{(1+az+bz^2)(1+cz+dz^2)}{(1-z)^6}.
\]
In particular the dimension is five, and its normalized volume is
\[
5!\operatorname{vol}_5(J)=h_J^*(1)=(a+b+1)(c+d+1)=NM.
\]
These generating-function identities are known background results, not claimed as new.

**2. Exact coefficients and their signs.** Multiply the numerator and expand using the polynomial identity
\[
L_J(n)=\sum_{j=0}^{4}h_j\binom{n+5-j}{5},
\quad (h_0,h_1,h_2,h_3,h_4)=(1,a+c,ac+b+d,ad+bc,bd).
\]
Straight expansion gives the complete coefficient identities
\[
\begin{array}{rl}
[n^0]L_J(n)&=1,\\
[n]L_J(n)&=U/60,\\
[n^2]L_J(n)&=V/24,\\
[n^3]L_J(n)&=\bigl((a-b)(c-d)+7(a+c)+b+d+17\bigr)/24,\\
[n^4]L_J(n)&=\bigl(ac-bd+2(a+c)+b+d+3\bigr)/24,\\
[n^5]L_J(n)&=NM/120.
\end{array}
\]
The cubic coefficient is positive because \(a-b,c-d\ge0\); the quartic coefficient is positive because \(ac\ge bd\); the leading and constant coefficients are positive. This proves the two-inequality criterion for all admissible polygons.

**3. Reduction of the sharp cutoff to a finite exhaustive integer proposition.** With \(N=a+b+1\) and \(M=c+d+1\), and after interchanging factors if needed, assume \(1\le N\le M\). The only restrictions used for the cutoff are
\[
N,M\in\mathbb Z_{\ge1},\quad
0\le b\le\left\lfloor\frac{N-1}2\right\rfloor,\quad
0\le d\le\left\lfloor\frac{M-1}2\right\rfloor,
\]
with \(a=N-1-b\) and \(c=M-1-d\). Every actual lattice-polygon pair lies in this integer parameter domain, although the domain also contains nonrealizable Pick data. The sign numerators simplify to
\[
\begin{aligned}
U&=-3NM+15(N+M)+110+5b(M-4-2d)+5d(N-4),\\
V&=-NM+11(N+M)+24+b(M-12)+d(N-12).
\end{aligned}
\]
For \(NM\le167\), the integer loops in the included \(\texttt{verify.py}\) visit **every** tuple in this larger domain: they iterate \(N\) from \(1\) to \(167\), \(M\) from \(N\) to \(\lfloor167/N\rfloor\), and then all \(b,d\) in their complete allowed integer ranges. Exactly **14,438** states are visited; the global minimum of \(U\) is **5**, attained at \((N,M,b,d)=(11,15,0,0)\), and the global minimum of \(V\) is **45** at \((1,1,0,0)\). This is an exhaustive finite proof of the volume-bounded assertion, not a sampled search or an extrapolation to unbounded volume.

Running the same exhaustive loops through \(NM\le168\) visits **14,838** states. The **unique** tuple with \(U\le0\) or \(V\le0\) is \((N,M,b,d)=(12,14,0,0)\), with \((U,V)=(-4,142)\). Since the displayed triangles have these data, they give an attainable sharp counterexample at normalized volume \(168\). This also establishes the claimed uniqueness of the offending Ehrhart-data type at the cutoff.

**4. Independence of the sign obstructions.** For the first example, \((a,b,c,d)=(11,0,13,0)\), so \((U,V)=(-4,142)\). The second example has \((a,b,c,d)=(11,0,78,78)\): its second triangle has three primitive edges and determinant \(157\), hence boundary count three and interior count \((157-3+2)/2=78\) by Pick's theorem. Here \((U,V)=(113,-1)\). All other coefficients are strictly positive by step 2.

## Verification

Run \(\texttt{python3 verify.py}\) in a directory containing the supplied standalone verifier. It uses only Python standard-library exact integer and rational arithmetic. It exhaustively checks the full relaxed Pick-data domain through normalized volume \(168\), reports the exact minima below the threshold and the unique violating tuple at the threshold, and recomputes six parameter examples in two independent ways: binomial-basis expansion of the numerator, and convolution of the two Pick Ehrhart polynomials followed by Newton interpolation. It also checks both exhibited sign patterns. The actual run reported:

```text
EXACT_OK below_168_states=14438 min_U=5 min_V=45 upto_168_states=14838 unique_bad=(12, 14, 0, 0, -4, 142) coeff_linear=-1/15 quadratic_only=-1/24 independent_convolutions=6
```

The correctness of the finite cutoff depends on the proven completeness of the loop domain and its exact execution. All-unbounded assertions in the two-inequality criterion follow algebraically, not from this bounded computation.

## Relationship to prior work

Liu, Tao, and Xin established that Ehrhart positivity need not survive a lattice join and gave an explicit example based on a four-dimensional cube joined with an interval; their main asymptotic theorem treats large dilations of factors of dimension at least four. Their general join-series identity is used here without novelty claim. The new mathematical content is the complete **two-dimensional-factor sign criterion**, the **sharp normalized-volume minimum \(168\)**, the **unique obstruction at that threshold**, and the **separation of linear and quadratic sign failures**. Later work by Liu and collaborators surveys Ehrhart properties under operations and repeats the same known join counterexample but does not determine this two-polygon cutoff in the inspected lattice-join section. The classical Pick formula and the known join product identity are explicitly credited as inputs. Searches of relevant published results did not reveal the exact sharp threshold; absence from the inspected sources is not a proof of historical priority.

## Limitations

The exact cutoff applies to standard joins of two full-dimensional **lattice polygons only**, rather than all five-dimensional lattice polytopes, all joins, or nonstandard lattice realizations. The finite enumeration proves the minimum after relaxing polygon realizability restrictions; its negative equality case is shown explicitly realizable. It does not classify lattice-equivalence classes of polygons with fixed Ehrhart data, and does not claim global novelty or independent validation. Historical coverage under other terminology remains possible.

## References

1. Feihu Liu, Sihao Tao, Guoce Xin, *Ehrhart Theory of the Join of Two Lattice Polytopes*, arXiv:2606.18794v1 (first public 2026-06-17), especially Definition 1.1, Proposition 1.2, Theorem 2.3 and Example 2.4. https://arxiv.org/abs/2606.18794
2. Feihu Liu et al., *Ehrhart Properties under Operations on Lattice Polytopes*, arXiv:2610.06338v1 (first public 2026-10-05), especially Section 3, Example 3.4. https://arxiv.org/abs/2610.06338
3. G. Pick, the classical lattice-polygon area formula (1899); used only in its standard \(\operatorname{area}=I+B/2-1\) form.
