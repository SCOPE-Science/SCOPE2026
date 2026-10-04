# Exact subthreshold Frobenius correction for primitive Pythagorean quadruples
## Finding
Let \(n,p\in\mathbb Z_{>0}\) be coprime and put \(Q=n^2+p^2\). Let \(m\) satisfy
\[
Q<m<2Q,\qquad \gcd(m,Q)=1,\qquad m+n+p\equiv1\pmod 2.
\]
Define
\[
S=\langle 2mn,2mp,m^2-Q,m^2+Q\rangle,
\qquad H=\langle n,p\rangle,
\qquad g_H=np-n-p,
\]
and set \(d=m-Q\). For every positive integer \(u\), define the two-gap spacing
\[
\lambda_H(u)=\min\{h\in H:h-u\in H\}.
\]
Then
\[
g(S)=(m+1)(m^2-Q)+2m\bigl(g_H-\lambda_H(d)\bigr).
\]
Equivalently, if
\[
G_0=m(m^2-Q)+2m(np-n-p)
\]
is the coprime formula proved by Hwang--Song for \(m\ge 2Q\), then throughout the adjacent band \(Q<m<2Q\),
\[
g(S)=G_0+E,\qquad E=(m^2-Q)-2m\lambda_H(m-Q)>0.
\]
Hence the boundary \(m=2Q\) is sharp as a universal threshold for the Hwang--Song formula: every admissible parameter in \(Q<m<2Q\) has a strictly larger Frobenius number.

The correction is explicit. If \(d\in H\), then \(\lambda_H(d)=d\). If \(d\notin H\), necessarily \(n,p>1\); let \(a\in\{1,\ldots,p-1\}\) and \(b\in\{1,\ldots,n-1\}\) be the unique residues satisfying
\[
an\equiv d\pmod p,\qquad bp\equiv d\pmod n.
\]
Then
\[
\lambda_H(d)=\min(an,bp).
\]

## Assumptions and scope
The theorem concerns the coprime case \(\gcd(n,p)=1\), under exactly the primitivity conditions \(\gcd(m,Q)=1\) and \(m+n+p\equiv1\pmod 2\), and only the contiguous subthreshold range \(Q<m<2Q\). In this range \(m^2-Q>0\), so all four displayed generators are positive. The result does not classify the range \(m\le Q\), nor the noncoprime case \(\gcd(n,p)>1\).

## Proof
Write
\[
B=m^2-Q,\qquad C=m^2+Q.
\]
Because \(H=\langle n,p\rangle\) has Frobenius number \(g_H=np-n-p<Q<m\), one has \(m\in H\). Also \(Q=n^2+p^2\in H\), hence \(B,C\in H\). The parity assumption makes \(B\) odd, while \(\gcd(B,m)=\gcd(Q,m)=1\); therefore \(\gcd(B,2m)=1\).

We first obtain an exact residue decomposition modulo \(2m\). Every element of \(S\) can be written as \(xB+yC+2mh\) with \(x,y\ge0\) and \(h\in H\). Since \(B+C=2m^2\), for the unique \(r\in\{0,\ldots,2m-1\}\) satisfying the residue condition modulo \(2m\), separating the cases \(x\ge y\) and \(x<y\) gives
\[
S\cap\bigl(rB+2m\mathbb Z\bigr)
 =\{rB+2mt:t\in H\cup(a_r+H)\},
\qquad a_r=m^2+Q-rm.
\]
Conversely, both pieces on the right are attained: \(rB+2mH\subset S\), while
\[
rB+2ma_r=(2m-r)C\in S.
\]
Thus, with
\[
\Gamma_r=\max\{t\in\mathbb Z:t\notin H,\ t-a_r\notin H\},
\]
one has
\[
g(S)=\max_{0\le r<2m}\bigl(rB+2m\Gamma_r\bigr).
\]

If \(0\le r\le m\), then \(a_r=m(m-r)+Q\in H\). Hence \(H\cup(a_r+H)=H\), so \(\Gamma_r=g_H\). Because \(B>0\), the largest contribution in this half is
\[
G_0=mB+2mg_H.
\]

Now let \(r=m+s\) with \(1\le s<m\), and put \(d_s=sm-Q\). Since \(m>Q\), every \(d_s\) is positive and \(a_{m+s}=-d_s\). The two-generated numerical semigroup \(H\) is symmetric: for every integer \(t\),
\[
t\notin H\quad\Longleftrightarrow\quad g_H-t\in H.
\]
Therefore
\[
\Gamma_{m+s}=g_H-\lambda_H(d_s),
\]
where \(\lambda_H(u)=\min\{h\in H:h-u\in H\}\). The contribution of this residue is consequently
\[
G_s=G_0+sB-2m\lambda_H(d_s).
\]
Since \(\lambda_H(d_s)\ge d_s\), for every \(s\ge2\),
\[
2m\lambda_H(d_s)-sB
\ge 2m(sm-Q)-s(m^2-Q)
=s(m^2+Q)-2mQ
\ge2\bigl(m(m-Q)+Q\bigr)>0.
\]
Thus \(G_s<G_0\) for all \(s\ge2\). Only \(s=1\) can exceed the central value.

Set \(d=m-Q\). Then
\[
G_1=G_0+B-2m\lambda_H(d).
\]
It remains to prove that the correction \(E=B-2m\lambda_H(d)\) is positive.

If \(d\in H\), then \(\lambda_H(d)=d\), and
\[
E=2mQ-m^2-Q.
\]
As a function of \(m\) this is concave. On the integer interval \(Q+1\le m\le2Q-1\), its endpoint values are \(Q^2-Q-1\) and \(Q-1\), both positive because \(Q\ge2\). Hence \(E>0\).

If \(d\notin H\), choose \(a\in\{1,\ldots,p-1\}\) with \(an\equiv d\pmod p\). Since \(d\notin H\), one must have \(an>d\), so \(an-d\in p\mathbb Z_{\ge0}\subset H\). Hence \(\lambda_H(d)\le an<np\). Using \(2np\le n^2+p^2=Q\),
\[
E=m^2-Q-2m\lambda_H(d)
>m^2-Q-mQ
=m(m-Q)-Q>0.
\]
Therefore \(G_1>G_0\), while all \(G_s\) with \(s\ge2\) lie below \(G_0\). The unique maximizing residue is \(r=m+1\), and
\[
g(S)=G_1=(m+1)B+2m\bigl(g_H-\lambda_H(d)\bigr).
\]

Finally, suppose \(d\notin H\). In a pair \(h,h-d\in H\) minimizing \(h\), write both as nonnegative combinations of \(n,p\). If both combinations use \(n\), subtracting \(n\) from both contradicts minimality; the same holds for \(p\). Since \(d\notin H\), the lower member is nonzero. Therefore a minimizing pair must be of one of the two crossed forms
\[
h=an,\quad h-d=kp,
\qquad\text{or}\qquad
h=bp,\quad h-d=\ell n.
\]
The least possible upper terms are precisely the least positive multiples satisfying the displayed congruences, giving \(\lambda_H(d)=\min(an,bp)\).

## Verification
The proof above is symbolic and does not depend on finite enumeration. A separate exact-integer checker evaluates \(\lambda_H\) both by its defining minimum and by the modular formula, and independently computes Frobenius numbers by shortest paths in residue classes. It verified 4,418 spacing instances and 743 admissible subthreshold quadruple instances with \(1\le n\le8\) and \(n\le p\le9\), with exact agreement in every case and strictly positive correction in every case. The smallest observed correction is \(1\), at \((n,p,m)=(1,1,3)\). Run `python verify.py`; the expected line is stored in `verification_output.txt`.

## Relationship to prior work
Hwang and Song determine the Frobenius number of this four-generator semigroup and, in the coprime case \(\gcd(n,p)=1\), prove
\[
g(S)=m(m^2-Q)+2m(np-n-p)
\]
under the hypothesis \(m\ge2Q\). Their second residue decomposition explicitly separates this coprime range from the weaker bound available when \(\gcd(n,p)>1\). The present theorem treats the immediately adjacent coprime regime \(Q<m<2Q\): it identifies the single residue \(r=m+1\) that becomes dominant, gives its exact two-gap correction, and proves that the correction is always strictly positive. Thus it is neither a specialization nor a consequence of their stated theorem, whose hypothesis excludes the entire regime considered here.

Earlier work on Pythagorean numerical semigroups cited by Hwang--Song concerns three-generator semigroups associated with primitive Pythagorean triples. Those results do not contain the four-generator residue decomposition above or imply the subthreshold correction for primitive Pythagorean quadruples.

## Limitations
The result does not determine \(g(S)\) when \(m\le Q\), where the signs and residue competition change, nor does it refine the \(\gcd(n,p)>1\) branch. The modular expression for \(\lambda_H\) uses the special symmetry of a two-generated coprime numerical semigroup. The finite checker supports but does not replace the universal proof. Literature searches cannot establish absolute novelty; the closest directly relevant source located is Hwang--Song's 2026 preprint, whose full text was inspected through its main theorem and residue-decomposition proof and does not state this subthreshold formula.

## References
1. WonTae Hwang and Kyunghwan Song, “Frobenius Numbers Associated with Primitive Pythagorean Quadruples,” arXiv:2609.21397v1, 18 September 2026. Primary MSC 11D07.
2. Edgar Federico Elizeche and Amitabha Tripathi, “On numerical semigroups generated by primitive Pythagorean triplets,” Integers 20 (2020), A75.
3. Byung Keon Gil et al., “Frobenius numbers of Pythagorean triples,” International Journal of Number Theory 11 (2015), 613–619.
