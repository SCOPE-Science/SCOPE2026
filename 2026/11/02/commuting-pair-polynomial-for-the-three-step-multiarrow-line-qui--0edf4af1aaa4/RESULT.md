# Commuting-pair polynomial for the three-step multiarrow line quiver

## Finding

Let \(q\) be any prime power. For integers \(r,s,t\geq1\), let \(Q_{r,s,t}\) be the four-vertex acyclic quiver with \(r\) distinct arrows from vertex \(0\) to \(1\), \(s\) arrows from \(1\) to \(2\), and \(t\) arrows from \(2\) to \(3\), and no other arrows. Let \(J\) be the Jacobson radical of its path algebra \(\mathbb F_q Q_{r,s,t}\). This radical has dimension \(r+s+t+rs+st+rst\) and nilpotency index \(4\).

The following finite formula counts **all ordered pairs** \((X,Y)\in J^2\) with \(XY=YX\), including zero elements. Define
\[
D=2rs+2st,\qquad W=2rst,\qquad E(i,j)=s(it+rj-ij).
\]
For each integer \(d\geq1\), define
\[
N_d(0)=1,\quad N_d(1)=(q+1)(q^d-1),\quad
N_d(2)=(q^d-1)(q^d-q).
\]
Then, for all indicated \(q,r,s,t\), the commuting-pair count is exactly
\[
\begin{aligned}
C_{r,s,t}(q)=q^W\bigg[&\sum_{i=0}^2\sum_{j=0}^2 N_r(i)N_t(j)q^{D-E(i,j)}\\
&+(q+1)(q^s-1)\big\{q^D+(q^r-1)q^{D-st}
 +(q^t-1)q^{D-sr}\\
&\hspace{26mm}+(q^r-1)(q^t-1)q^{D-s(r+t-1)}\big\}\\
&+(q^s-1)(q^s-q)q^D\bigg].
\end{aligned}
\]
All terms have nonnegative integer powers of \(q\), so \(C_{r,s,t}(q)\in\mathbb Z[q]\). Equivalently, if \(P\) is the direct sum of the four indecomposable projective representations, the same polynomial is the commuting-pair invariant \([Q_{r,s,t},(1,1,1,1)]\) of the radical of \(\operatorname{End}(P)\).

The one-arrow specialization \(r=s=t=1\) is \(q^7(2q^2+q-2)\), the classical four-by-four unitriangular case. This specialization is **not** asserted to be new. The claim concerns the general positive multiplicities \(r,s,t\).

## Assumptions and scope

The finite field may have any characteristic, including characteristic two; no assumption on algebraic closure is made. Paths are concatenated in the forward order when endpoints match. Reversing the convention passes to the opposite algebra and leaves the commuting-pair count unchanged. In \(J^2\), the superscript denotes the Cartesian square \(J\times J\), not the product ideal. All vertex projectives have multiplicity one, even when arrow multiplicities are arbitrary.

## Proof

Write \(A=\mathbb F_q^r\), \(B=\mathbb F_q^s\), and \(C=\mathbb F_q^t\) for the spaces of arrows in the three consecutive layers. The positive-length paths in the radical give a direct sum of vector spaces
\[
J=(A\oplus B\oplus C)\oplus (A\otimes B\oplus B\otimes C)\oplus(A\otimes B\otimes C).
\]
Write two arbitrary radical elements as
\[
X=(a,b,c,u,v,w),\qquad Y=(a',b',c',u',v',w'),
\]
where \(a,a'\in A\), \(b,b'\in B\), \(c,c'\in C\), \(u,u'\in A\otimes B\), \(v,v'\in B\otimes C\), and \(w,w'\in A\otimes B\otimes C\).
The basis of distinct directed paths and concatenation give **exactly** three commutator conditions:
\[
a\otimes b'-a'\otimes b=0,\qquad
b\otimes c'-b'\otimes c=0,
\]
\[
a\otimes v'-a'\otimes v+u\otimes c'-u'\otimes c=0.
\]
There are no other conditions; the two longest-path variables \(w,w'\) are completely free, giving \(q^W\) choices.

Fix \(a,a',b,b',c,c'\) satisfying the first two conditions. Put \(i=\dim\langle a,a'\rangle\) and \(j=\dim\langle c,c'\rangle\), both in \(\{0,1,2\}\). The linear map from the four second-layer variables \((u,u',v,v')\) to the last displayed commutator coefficient has image
\[
\langle a,a'\rangle\otimes B\otimes C
 + A\otimes B\otimes\langle c,c'\rangle.
\]
The two summands intersect in \(\langle a,a'\rangle\otimes B\otimes\langle c,c'\rangle\). Therefore its rank is \(E(i,j)=s(it+rj-ij)\). Since its domain dimension is \(D=2rs+2st\), precisely \(q^{D-E(i,j)}\) second-layer choices satisfy the third equation. This is a surjectivity statement about the displayed image, not a heuristic dimension estimate.

It remains to enumerate the first-layer solutions by the rank \(h=\dim\langle b,b'\rangle\) of the middle arrow pair. If \(h=0\), the pairs \((a,a')\) and \((c,c')\) are unrestricted. The numbers with spans of dimensions \(i\) and \(j\) are respectively \(N_r(i)\) and \(N_t(j)\), the standard rank counts for a matrix with two columns. This gives the double sum in the displayed formula.

If \(h=1\), there are \((q+1)(q^s-1)\) middle pairs: first choose their common projective coefficient line in \(\mathbb F_q^2\), then choose a nonzero middle vector. The first commutator equation forces \((a,a')\) to have this same coefficient line (or to vanish); similarly the second equation forces \((c,c')\) onto the same line (or to vanish). For a fixed line there are \(q^r\) possible endpoint vectors and \(q^t\) at the other endpoint. Separating the four possibilities (zero/positive endpoint vectors) yields exactly the four terms inside braces, with ranks \((i,j)=(0,0),(1,0),(0,1),(1,1)\).

If \(h=2\), both endpoint pairs must vanish by the two tensor equations; there are \(N_s(2)=(q^s-1)(q^s-q)\) middle pairs, and the second layer is unrestricted, contributing the final term. The three cases are disjoint and exhaustive, proving the formula. All exponents are nonnegative by the rank-of-linear-map argument. Finally, since \(P\) is the projective generator, \(\operatorname{End}(P)\) is isomorphic to the opposite path algebra. Radical multiplication is reversed, but commutativity is not, so the quiver commuting-pair invariant coincides with \(C_{r,s,t}(q)\).

## Verification

The standalone program `verify.py` independently constructs a basis of all nonempty paths and directly tests whether products commute, without using the rank stratification for its enumeration. It checks the closed formula for \((q,r,s,t)=(2,1,1,1),(3,1,1,1),(2,2,1,1),(2,1,2,1)\), obtaining respectively \(1024\), \(41553\), \(30208\), and \(108544\) commuting ordered pairs. It uses ordinary prime fields; the algebraic proof covers every prime power. For further symbolic spot checks, the formula gives
\[
C_{1,1,1}(q)=q^7(2q^2+q-2),\qquad
C_{2,1,1}(q)=q^9(q^5+2q^4+q^3-3q^2-q+1).
\]
Run `python3 verify.py` from the directory containing the file. No third-party packages are required.

## Relationship to prior work

Hennecart and Perry introduced the commuting-radical-endomorphism version of Higman's conjecture and gave formulas for quivers with no paths longer than two, alongside count-preserving quiver operations. Here every arrow multiplicity is positive and there is a path of length three; the new count is not a specialization of the displayed length-at-most-two formulas. Pak and Soffer computed conjugacy-class counts for classical unitriangular groups, which already cover the \((1,1,1)\) specialization. The present formula extends beyond a single ordinary chain to three independently variable parallel-arrow multiplicities. Green and Schroll's *commuting algebra* refers to a quotient imposing equality of parallel paths, a different multiplication problem. No claim is made that general Higman polynomiality is solved.

## Limitations

The theorem treats the full path algebra with all vertex-projective multiplicities equal to one; it does not count for arbitrary projective summand vectors, arbitrary acyclic quivers, or imposed path relations. The formula is a formal polynomial identity for each fixed triple of positive integers, not a positivity statement about its ordinary coefficients. Existing general tensor-invariant or pattern-group methods could conceivably imply the formula without the same explicit presentation; the available primary literature comparison did not establish such coverage. Independent mathematical audit and publication-priority confirmation have not been performed.

## References

1. L. Hennecart and N. Perry, *A Quiver Analogue of Higman's Conjecture*, arXiv:2208.07738 (first posted 2022-08-16), especially Sections 3–5, https://arxiv.org/html/2208.07738v1.
2. I. Pak and A. Soffer, *On Higman's \(k(U_n(\mathbb F_q))\) Conjecture*, arXiv:1507.00411 (first posted 2015-07-02), especially Sections 1 and 6.3, https://arxiv.org/html/1507.00411v1.
3. E. L. Green and S. Schroll, *The Commuting Algebra*, arXiv:2302.08169 (2023), https://arxiv.org/abs/2302.08169.
