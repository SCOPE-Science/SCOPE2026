# Exact centralizer spectrum and commutativity degree of the finite Jacobson–Witt algebra \(W_1\)
## Finding
Let \(p>3\) be a prime, let \(q=p^e\), and put
\[
A=\mathbb F_q[x]/(x^p),\qquad W=\operatorname{Der}_{\mathbb F_q}(A)=A\partial,
\]
where \(\partial=d/dx\). Thus every element of \(W\) has a unique form \(f\partial\) with \(f\in A\), and
\[
[f\partial,g\partial]=(fg'-gf')\partial.
\]
Write \(m=(p-1)/2\). For nonzero \(f\), let \(s=v_x(f)\in\{0,\ldots,p-1\}\). Then
\[
\dim_{\mathbb F_q} C_W(f\partial)=
\begin{cases}
1,&s=0,\\
s,&1\le s\le m,\\
s-1,&m+1\le s\le p-1.
\end{cases}
\]
The zero element has centralizer dimension \(p\). Therefore the complete centralizer-dimension multiplicity distribution is
\[
N_d=
\begin{cases}
(q^2-1)q^{p-2},&d=1,\\
(q-1)q^{p-d-1},&2\le d<m,\\
(q^2-1)q^{m-1},&d=m,\\
(q-1)q^{p-d-2},&m<d\le p-2,\\
1,&d=p,\\
0,&\text{otherwise}.
\end{cases}
\]
In particular there is no element with centralizer dimension \(p-1\). The number of ordered commuting pairs is
\[
\#\{(D,E)\in W^2:[D,E]=0\}=q^{p-2}\bigl(q^3+m(q^2-1)\bigr),
\]
and hence the commutativity degree is
\[
\operatorname{cd}(W)=\frac{q^3+m(q^2-1)}{q^{p+2}}.
\]
The regular elements are exactly the two valuation strata \(v_x(f)=0\) and \(v_x(f)=1\); their number is \((q^2-1)q^{p-2}\), so their density is \(1-q^{-2}\).

## Assumptions and scope
The result concerns the one-variable Jacobson–Witt algebra over an arbitrary finite field \(\mathbb F_q\) of characteristic \(p>3\). It counts Lie centralizers in \(W\), not stabilizers in the automorphism group, and it counts all commuting ordered pairs, not only nilpotent commuting pairs. The proof is uniform in the extension degree \(e\).

## Proof
Fix a nonzero \(f\in A\). There is a unique \(s=v_x(f)\) and a unit \(u\in A^\times\) such that \(f=x^s u\). Multiplication by \(u\) is a vector-space bijection, so write an arbitrary \(g\in A\) as \(g=uh\).

If \(s=0\), then
\[
fg'-gf'=u^2h'.
\]
Because the basis of \(A\) is \(1,x,\ldots,x^{p-1}\) and each integer \(1,\ldots,p-1\) is nonzero in characteristic \(p\), the kernel of \(h\mapsto h'\) consists exactly of the constants. Thus the centralizer has dimension \(1\).

Now suppose \(1\le s\le p-1\). The unit terms cancel:
\[
(x^su)(uh)'-(uh)(x^su)'=u^2x^{s-1}(xh'-sh).
\]
Hence \([f\partial,g\partial]=0\) if and only if
\[
x^{s-1}(xh'-sh)=0\quad\text{in }A.
\]
Writing \(h=\sum_{i=0}^{p-1}a_i x^i\), this becomes
\[
(i-s)a_i=0\qquad(0\le i\le p-s).
\]
The coefficients \(a_i\) with \(p-s+1\le i\le p-1\) are unconstrained, giving \(s-1\) free coordinates. Among the remaining indices, \(i-s\) vanishes in \(\mathbb F_q\) only at \(i=s\), and that index is present exactly when \(2s\le p\), equivalently \(s\le m\). This proves the centralizer-dimension formula.

For a fixed valuation \(s\), the number of nonzero \(f\in A\) with \(v_x(f)=s\) is
\[
(q-1)q^{p-s-1}.
\]
Grouping these valuation strata by their centralizer dimensions gives the displayed multiplicities. At the middle dimension \(d=m\), the two adjacent valuations \(s=m\) and \(s=m+1\) contribute
\[
(q-1)(q^m+q^{m-1})=(q^2-1)q^{m-1}.
\]
All multiplicities sum to \(q^p\).

Finally, summing centralizer sizes over all elements gives the commuting-pair count. The zero element contributes \(q^p\). The valuations \(s=0,1\) together contribute \((q^2-1)q^{p-1}\). Each \(s\) with \(2\le s\le m\) contributes \((q-1)q^{p-1}\), and each \(m+1\le s\le p-1\) contributes \((q-1)q^{p-2}\). Therefore
\[
\sum_{D\in W}|C_W(D)|
=q^{p-2}\bigl(q^3+m(q^2-1)\bigr).
\]
Dividing by \(|W|^2=q^{2p}\) yields the stated commutativity degree.

## Verification
The accompanying checker constructs the bracket matrix directly from the truncated-polynomial multiplication law. It exhaustively checks every one of the \(5^5=3125\) elements of \(W_1(\mathbb F_5)\), including the complete centralizer-dimension histogram and the commuting-pair total \(21625\). It also checks ninety non-monomial representatives in characteristics \(7\) and \(11\), and separately tests the unit-cancellation identity used in the proof in characteristics \(5,7,11\). The checker returned `VERIFY_OK`.

These finite checks are consistency tests only. The theorem for every finite extension \(\mathbb F_{p^e}\) follows from the symbolic argument above; no exhaustive computation over extension fields is used as an infinite proof.

## Relationship to prior work
Premet studies regular derivations of truncated polynomial rings and defines regularity by minimal Lie-centralizer dimension. For the Jacobson–Witt algebra he proves a broad regularity criterion over an algebraically closed field and identifies the derivation algebra structurally. The present result instead gives the complete finite-field centralizer-size distribution in the one-variable case and its exact rational-point sum.

Chang's work on adjoint quotient maps for \(W_n\) likewise treats regularity, invariant theory, and the algebraic geometry of fibers. Skryabin counts nilpotent elements of Jacobson–Witt algebras over finite fields. Those results do not state the all-element centralizer multiplicities above.

Yao and Chang later study the commuting variety of the same one-variable Witt algebra over an algebraically closed field and determine its irreducible components and their dimensions. That is the closest object-level comparison found. Their published abstract describes geometric components and dimensions, not finite-field point counts or a commutativity degree. The full text was not available through the accessible open route during this check, so a residual risk remains that intermediate centralizer lemmas overlap some unweighted strata. The exact finite-field multiplicities and the closed commuting-pair formula were not located. A later paper introducing commutativity degree for finite-dimensional Lie algebras over finite fields gives the general averaging identity and examples, but its searchable full text contains no occurrence of “Witt” or “Jacobson”.

## Limitations
The theorem is restricted to the one-variable Jacobson–Witt algebra and to characteristic \(p>3\). It does not count pairwise commuting \(r\)-tuples for \(r>2\), does not treat \(W_n\) for \(n>1\), and does not give the geometry of the commuting variety. The originality comparison against the 2018 same-object commuting-variety paper is limited by lack of accessible full text; the comparison is therefore strongest for the finite-field multiplicity and point-count statements rather than for every intermediate centralizer lemma.

## References
1. A. Premet, “Regular derivations of truncated polynomial rings,” arXiv:1405.2426, first submitted 10 May 2014; later in *Lie Algebras and Related Topics*, Contemporary Mathematics 652 (2015), 123–139. Primary MSC 17B50.
2. H. Chang, “Adjoint quotient maps for restricted Lie algebras \(W_n\) and \(S_n\),” arXiv:1405.3216, first submitted 13 May 2014.
3. S. Skryabin, “Nilpotent elements in the Jacobson–Witt algebra over a finite field,” *Transformation Groups* 19 (2014), 927–940, DOI 10.1007/s00031-014-9270-0.
4. Y.-F. Yao and H. Chang, “Commuting variety of Witt algebra,” *Frontiers of Mathematics in China* 13 (2018), 1179–1187, DOI 10.1007/s11464-018-0725-9.
5. A. Shamsaki, A. Erfanian, and M. Parvizi, “On the commutativity degree of a finite-dimensional Lie algebra,” arXiv:2406.10064.
