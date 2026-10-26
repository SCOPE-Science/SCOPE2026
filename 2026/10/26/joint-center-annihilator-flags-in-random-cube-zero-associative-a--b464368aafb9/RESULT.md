# Joint center–annihilator flags in random cube-zero associative algebras over finite fields

## Finding
Let \(q\) be any prime power and \(r,s\ge1\) with \(s\le r^2\). Choose uniformly among surjective \(\mathbb F_q\)-linear maps \(B:V\otimes V\to W\), where \(\dim V=r\), \(\dim W=s\). Define the nonunital associative algebra \(A_B=V\oplus W\) by \((v,w)(v',w')=(0,B(v,v'))\). This has \(A_B^3=0\) and \(A_B^2=W\). Let \(T=\operatorname{Ann}(A_B)/W\) and \(U=Z(A_B)/W\), both viewed in \(V\). We count the **joint nested flag** \(T\subseteq U\), not just either dimension separately.

Write \({n\brack k}_q\) for a Gaussian binomial coefficient and define \(F_q(d,s)=\prod_{h=0}^{s-1}(q^d-q^h)\) for \(d\ge s\), and zero otherwise. For \(0\le a\le b\le r\), put
\[
D_r(a,b)=(r-a)^2-(b-a)(r-b)-\binom{b-a}{2}.
\]
For each \(0\le t\le u\le r\), the **exact number of surjective products** with \(\dim T=t\) and \(\dim U=u\) is
\[
N_{r,s,q}(t,u)={r\brack u}_q{u\brack t}_q
\sum_{i=0}^{u-t}\sum_{j=0}^{r-u}
(-1)^{i+j}q^{\binom i2+\binom j2}
{u-t\brack i}_q{r-u\brack j}_q
F_q(D_r(t+i,u+j),s).
\]
The joint probability is \(N_{r,s,q}(t,u)/F_q(r^2,s)\), and the counts sum to \(F_q(r^2,s)\). For each individual prescribed flag \(T\subseteq U\) of dimensions \(t,u\), the double sum is exactly the number of products realizing that particular flag.

Two consequences emphasize that the center and annihilator carry different information. If \(s=1\) and \(r\) is odd, then \(U\ne0\) for every product, in every characteristic. For fixed \(q\) and fixed \(s\ge2\), as \(r\to\infty\),
\[
\Pr(U\ne0)\sim {r\brack1}_q q^{-s(r-1)},\qquad
\Pr(T\ne0\mid U\ne0)\sim q^{-sr}.
\]
Consequently \(U=0\) with probability tending to one when \(s\ge2\), in contrast to the odd-dimensional one-output case.

## Assumptions and scope
The algebra is associative since every product lies in \(W\), which annihilates the entire algebra. The tensor is **uniformly surjective**; this is a condition on its entire image, not an independent-entry approximation. \(\operatorname{Ann}(A)\) means the two-sided annihilator, and \(Z(A)=\{a\in A:ab=ba\text{ for every }b\in A\}\) is the associative center. The theorem counts labeled products on fixed \(V,W\), not isomorphism classes; no restriction on the characteristic of the field is made. The asymptotics hold only when \(q,s\) are fixed and \(r\to\infty\).

## Proof
**Linear condition count.** Fix subspaces \(S\subseteq X\subseteq V\) of dimensions \(a,b\). The inclusion \(S\subseteq T\) says \(B(S,V)=B(V,S)=0\), so \(B\) descends to a bilinear map on \(V/S\). This leaves \((r-a)^2\) free scalar coefficients. The inclusion \(X\subseteq U\) additionally demands \(B(x,v)=B(v,x)\) for all \(x\in X\), \(v\in V\). The commutator of a bilinear form is alternating, also in characteristic two. On \(V/S\), the restriction that its radical contain \(X/S\), of dimension \(b-a\), consists of \((b-a)(r-b)+\binom{b-a}{2}\) independent homogeneous linear equations. These are independent because the map from all bilinear forms to alternating forms, \(B\mapsto B-B^{\mathrm T}\), is surjective in every characteristic: use arbitrary upper-triangular entries and zero diagonal. Thus the permitted scalar-form space has dimension exactly \(D_r(a,b)\).

Writing the \(W\)-valued product in any fixed basis of \(W\) produces an ordered \(s\)-tuple of scalar forms from this space. The product has image all of \(W\) precisely when the \(s\) forms are independent. Their number is \(F_q(D_r(a,b),s)\); when the dimension is smaller than \(s\) there are none. This proves the fixed-containment count without treating finite experiments as proof.

**Exact flag by two Möbius inversions.** Fix a proposed flag \(T_0\subseteq U_0\) of dimensions \(t,u\). First impose \(T\supseteq S\) for an arbitrary \(S\subseteq U_0\), and apply Möbius inversion to the condition \(U\supseteq U_0\), along every larger central subspace \(X\supseteq U_0\). The subspace-lattice Möbius function across a codimension-\(j\) interval is \((-1)^jq^{\binom j2}\); there are \({r-u\brack j}_q\) choices for \(X\). This inversion counts products satisfying \(T\supseteq S\) and \(U=U_0\). Now invert the condition \(T\supseteq T_0\) over \(T_0\subseteq S\subseteq U_0\), using \((-1)^iq^{\binom i2}\), with \({u-t\brack i}_q\) choices for \(S\). Here \(S\subseteq X\) automatically, so the containment count from the preceding paragraph applies with dimensions \(t+i,u+j\). The resulting double sum counts the products with exactly \((T,U)=(T_0,U_0)\). There are \({r\brack u}_q{u\brack t}_q\) proposed flags, and the general linear group acts transitively on them, proving the formula and its normalization.

**Asymptotics.** For a fixed one-dimensional \(L\subset V\), the exact probability that \(L\subseteq U\) is \(F_q(r^2-(r-1),s)/F_q(r^2,s)\), asymptotic to \(q^{-s(r-1)}\). Thus the expected number of lines in \(U\) is \({r\brack1}_q q^{-s(r-1)}(1+o(1))\). For two distinct lines, their span has dimension two, so the joint probability is asymptotic to \(q^{-s(2r-3)}\). The number of unordered pairs is \(O(q^{2r})\); the ratio of the aggregate pair term to the first moment tends to zero for \(s\ge2\). Bonferroni's inequalities therefore give the first asserted probability asymptotic.

Likewise, a fixed line lies in \(T\) with exact probability \(F_q((r-1)^2,s)/F_q(r^2,s)\sim q^{-s(2r-1)}\). For two distinct lines the joint probability is \(F_q((r-2)^2,s)/F_q(r^2,s)\sim q^{-s(4r-4)}\), whose total pair contribution is negligible relative to the first moment for any fixed \(s\ge1\). Hence \(\Pr(T\ne0)\sim{r\brack1}_q q^{-s(2r-1)}\). Since \(T\subseteq U\), dividing by the center probability gives the conditional asymptotic \(q^{-sr}\). Finally, when \(s=1\), the commutator form is represented by one alternating \(r\)-by-\(r\) matrix. Its rank is even in every characteristic, so for odd \(r\) its radical \(U\) cannot vanish. This completes the proof.

## Verification
A standalone script `verify_joint.py` computes the formula using exact integer arithmetic and independently enumerates all tensors in seven small prime-field cases. It constructs the multiplication tensor entry by entry, tests surjectivity by row reduction, and computes the center and two-sided annihilator dimensions from separate commutator and left/right linear systems. The exhaustive cases are \((q,r,s)=(2,1,1),(2,2,1),(2,2,2),(2,3,1),(2,3,2),(3,2,1),(3,2,2)\). All joint coefficients match, including \(260610\) surjective tensors at \((q,r,s)=(2,3,2)\). The code uses prime fields, whereas the proof includes every prime-power field. The general claim rests on the two inversions and alternating-form rank argument, not on these finite tests.

## Relationship to prior work
Bahturin and Olshanskii (2024) develop generic properties of nilpotent algebras over finite fields, including typicality and ideal-theoretic questions, but their inspected introduction and Section 8 do not give this exact joint center–annihilator flag distribution. Ignatyev–Kaygorodov–Popov (2021) study geometric classifications of two-step nilpotent algebras and strata involving annihilator dimensions over algebraically closed fields, rather than finite-field point counts of the two nested subspaces. Verhulst (2020) counts isomorphism classes of general finite-field algebras via group actions, a distinct enumeration. Classical alternating-form rank counts address the center in the single-output case but not its joint dependence on the two-sided annihilator under a surjective multi-output tensor.

Earlier exact **two-sided annihilator** marginal counts in square-cube-zero algebras are prior work, not an originality claim here. The new invariant is the full joint flag and, in particular, the conditional occurrence of nonzero annihilator given a nonminimal center. The single marginal cannot recover this conditional law. The formula is not an isomorphism-orbit count.

## Limitations
This does not classify algebras up to isomorphism or give a closed elementary expression for every flag coefficient beyond the finite Gaussian double sum. The finite testing script covers prime fields and small dimensions only. The asymptotic estimates are fixed-field, fixed-output-dimension results, and do not cover growing \(s\). Although the listed primary papers were inspected in relevant full-text portions, a historically equivalent subspace-lattice inversion under alternative terminology cannot be excluded; no exhaustive publication-priority assertion or independent scientific audit is made.

## References
- Yu. Bahturin and A. Olshanskii, *On generic properties of nilpotent algebras*, arXiv:2406.15631v1 (first public June 21, 2024), https://arxiv.org/abs/2406.15631 .
- M. Ignatyev, I. Kaygorodov, and Yu. Popov, *The geometric classification of 2-step nilpotent algebras and applications*, arXiv:2103.01036, https://arxiv.org/abs/2103.01036 .
- W. Verhulst, *Counting Finite-Dimensional Algebras Over Finite Fields* (2020), open-access article concerning the isomorphism-class orbit problem.
- Standard Gaussian-binomial and subspace-lattice Möbius inversion identities; the latter is proved by induction from the defining lattice inversion relation.
