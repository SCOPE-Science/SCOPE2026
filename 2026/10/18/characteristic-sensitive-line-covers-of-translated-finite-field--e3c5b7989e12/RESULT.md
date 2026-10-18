# Characteristic-sensitive line covers of translated finite-field parabolas

## Finding
Let \(k=\mathbb F_q\), let \(2\le \ell\le q\), and let \(c_1,\ldots,c_\ell\in k\) be distinct. Let \(C\subset\mathbb P^2_k\) be the reduced union of the smooth projective conics \(YZ=X^2+c_iZ^2\). Write \(\operatorname{cov}_k(C)\) for the minimum number of \(k\)-projective lines covering every point of \(C(k)\).

**Odd characteristic.** For every odd prime power \(q\),
\[
\operatorname{cov}_k(C)\ge (q+3)/2.
\]
For \(\ell=2\), \((c_1,c_2)=(0,1)\), equality holds for each of the eight prime fields with \(q\in\{3,5,7,11,13,17,19,23\}\); exact covering witnesses are recorded in `verify.py`. No equality claim is made for arbitrary odd prime powers.

**Even characteristic.** For \(q=2^r\), \(r\ge2\), put \(V=\operatorname{span}_{\mathbb F_2}\{c_i-c_1:2\le i\le\ell\}\subset k\). If \(V\ne k\), then
\[
\operatorname{cov}_k(C)=q/2+1.
\]
In particular, this equality holds for **every** \(q=2^r\) with \(r\ge2\) when \(\ell=2\). For \(q=2\) and \(\ell=2\), it also holds: the two vertical lines suffice.

The contrast is exact: two distinct translated parabolas over any even field require precisely \(q/2+1\) lines, while their counterparts in every odd field require at least one additional line; the improved odd bound is attained over the eight specified prime fields.

## Assumptions and scope
The curves are unions of \(\ell\) geometrically irreducible smooth conics, but the union itself is reducible over \(k\); do not apply an irreducible-curve covering theorem to it. All affine components \(y=x^2+c_i\) have disjoint \(k\)-affine point sets and share the sole projective point \(P_\infty=[0:1:0]\). Thus \(|C(k)|=\ell q+1\). A nonvertical affine line contains at most two points of any one component. A vertical line contains one affine point on each component plus \(P_\infty\). The projective line at infinity contains only \(P_\infty\) from \(C(k)\).

## Proof
**1. Universal capacity bound.** Any cover includes at least one line through \(P_\infty\). If it contains \(r\ge1\) such lines among a total of \(m\), it covers at most \(1+\ell r+2\ell(m-r)\) distinct points: each line through infinity contributes no more than \(\ell\) affine points and every other line at most \(2\ell\). In particular \(m>q/2\), hence \(m\ge q/2+1\) for even \(q\) and \(m\ge(q+1)/2\) for odd \(q\).

**2. Odd-characteristic obstruction at the capacity threshold.** Suppose \(q\) is odd and \(m=(q+1)/2\). Then the capacity expression forces \(r=1\), and equality throughout forces the unique line through \(P_\infty\) to be a vertical line \(x=x_0\). Every remaining line \(L_j:y=s_jx+b_j\), \(1\le j\le h=(q-1)/2\), must meet **every** component in exactly two distinct affine points. These intersections are pairwise disjoint and, on each component, their \(x\)-coordinates partition \(k\setminus\{x_0\}\).

For component \(i\), the two abscissas cut out by \(L_j\) are roots of \(x^2-s_jx+(c_i-b_j)=0\). Their sum is \(s_j\), their product is \(c_i-b_j\), and their sum of squares is \(s_j^2-2(c_i-b_j)\). Summing over all \(j\), the result is the same number \(\sum_{x\ne x_0}x^2\) for every component. Subtracting the identities for distinct components \(i,i'\) gives
\[
0=-2h(c_i-c_{i'})=c_i-c_{i'}\quad\text{in }k,
\]
where \(2h=q-1=-1\) in characteristic dividing \(q\). This contradicts distinctness. Hence \(m\ge(q+3)/2\), for **all odd prime powers**, not just prime fields.

**3. Even-characteristic construction.** Suppose \(q=2^r\) with \(r\ge2\) and \(V\ne k\). The field trace pairing \((u,v)\mapsto\operatorname{Tr}_{k/\mathbb F_2}(uv)\) is nondegenerate. Choose \(t\in k^\times\) orthogonal to \(V\), then choose \(s\in k^\times\) with \(s^{-2}=t\) (squaring is bijective). The image
\[
H_s=\{x^2+sx:x\in k\}
=\{b\in k:\operatorname{Tr}_{k/\mathbb F_2}(b/s^2)=0\}
\]
has size \(q/2\); every difference \(c_i-c_1\) belongs to \(H_s\). Take the \(q/2\) pairwise parallel lines
\[
y=sx+b,\qquad b\in c_1+H_s.
\]
Every affine point \((x,x^2+c_i)\) lies on exactly one such line, because its intercept \(x^2+c_i-sx\) belongs to \(c_1+H_s\). Add any vertical line to cover \(P_\infty\). This yields \(q/2+1\) lines, exactly matching the general lower bound. If \(\ell=2\), \(V\) has dimension one, so it is proper for \(r\ge2\). Over \(\mathbb F_2\), the two vertical lines cover the two conics, proving the remaining case.

**4. Odd small-field equality witnesses.** For each \(q\in\{3,5,7,11,13,17,19,23\}\), `verify.py` lists \((q+3)/2\) lines, with `(s,b)` encoding \(y=sx+b\) and `('v',b)` encoding \(x=b\). The script checks every \((x,x^2+c)\) for \(c=0,1\) and every \(x\in\mathbb F_q\), plus coverage of \(P_\infty\) by a vertical line. Thus these are finite *upper-bound certificates*. The universal proof above supplies their lower bound without reliance on optimization software.

## Verification
Run `python3 verify.py` with the Python standard library. The checker exhaustively verifies the eight displayed odd-prime witness families. It also explicitly constructs and validates the parallel-line trace-kernel covers over \(\mathbb F_4,\mathbb F_8,\mathbb F_{16},\mathbb F_{32}\) using polynomial-basis arithmetic and checks the \(\mathbb F_2\) exception by inspection. Expected terminal text: `VERIFY_OK`. These finite cases corroborate the construction; the all-fields conclusions are proved algebraically, not inferred from experiments. The source code defines every finite-field operation and every listed witness.

## Relationship to prior work
Asgarli, Dassarma, Ghioca, MacLean, and Stokdyk (2026), Remark 1.4, introduce precisely this family of unions of translated parabolas to show that irreducibility is needed in their asymptotic theorem. They prove the capacity lower bound \(\operatorname{cov}_k(C)>q/2\), but not the parity-sensitive exact even-field formula, the odd-field second-moment obstruction, or explicit sharp odd-field covers. Their main theorem assumes \(k\)-irreducibility and therefore does **not** give upper bounds for these examples. The present result refines that specific sharpness example, without claiming their general line-cover theorem or any conic geometry as new.

## Limitations
For odd \(q\), equality beyond the eight displayed prime fields is not proved. For even \(q\) and larger \(\ell\) with \(V=k\), the exact minimum is not determined here. No assertion is made about all unions of arbitrary conics or about irreducible plane curves. The literature search did not identify an earlier identical covering calculation, but an unindexed finite-geometry argument could supply it. The exact optimal finite sets are independently reproducible; optimality rests on the stated mathematical lower bound.

## References
- Shamil Asgarli, Sarthak Dassarma, Dragos Ghioca, Simon MacLean, Evan Stokdyk, *Covering plane curves over finite fields with lines*, arXiv:2610.13042v1, October 9, 2026, especially Remark 1.4 and Theorem 1.2. https://arxiv.org/pdf/2610.13042
- For field-trace facts, see any standard finite-fields treatment; only the elementary Artin–Schreier image identity and nondegeneracy of the trace pairing are needed, and both follow from the degree-two additive map \(x\mapsto x^2+x\).
