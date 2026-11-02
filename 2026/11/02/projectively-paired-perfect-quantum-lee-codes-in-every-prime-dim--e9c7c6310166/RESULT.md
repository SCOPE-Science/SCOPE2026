# Projectively paired perfect quantum Lee codes in every prime dimension congruent to one modulo four

## Finding

**Theorem.** Let \(p\) be a prime with \(p\equiv1\pmod4\), and let \(r\ge2\) be an integer. There is an explicitly specified pure (nondegenerate at radius one) \(p\)-level stabilizer code of parameters
\[
\boxed{[[n,n-r,3_{\diamond}]]_p,\qquad n=(p^r-1)/4.}
\]
Here \(d_{\diamond}\) denotes the *joint Lee distance* in the standard computational Pauli frame. The code is perfect: its radius-one joint-Lee errors have distinct syndromes and fill all \(p^r\) syndromes; equivalently,
\[
p^{n-r}(1+4n)=p^n.
\]

There is also a sharp congruence obstruction *within the coordinatewise-collinear class*: for any odd prime \(p\), if a perfect radius-one stabilizer check matrix \(H=(H_X\mid H_Z)\) over \(\mathbb F_p\) has each physical-coordinate column pair \(((H_X)_i,(H_Z)_i)\) linearly dependent, then \(p\equiv1\pmod4\). This is not a nonexistence theorem for general stabilizer matrices when \(p\equiv3\pmod4\).

For example, \((p,r)=(5,2),(5,3),(13,2)\) respectively gives \([[6,4,3_{\diamond}]]_5\), \([[31,28,3_{\diamond}]]_5\), and \([[42,40,3_{\diamond}]]_{13}\). The first parameter set also appears in the motivating literature, but the construction here extends to all stated \(p,r\).

## Assumptions and scope

All linear algebra is over the prime field \(\mathbb F_p\). An \(n\)-qudit Pauli operator is represented up to phase by \((u\mid v)\in\mathbb F_p^{2n}\), acting as \(X^uZ^v\). Its joint Lee weight is
\[
w_{\diamond}(u\mid v)=\sum_{i=1}^n\bigl(\min(\bar u_i,p-\bar u_i)+\min(\bar v_i,p-\bar v_i)\bigr),
\]
where bars are integer representatives in \(\{0,\dots,p-1\}\). Write \(J=\begin{pmatrix}0&I_n\\-I_n&0\end{pmatrix}\). An \(r\times2n\) stabilizer check matrix satisfies \(HJH^{\mathsf T}=0\); the syndrome of \(e\) is \(HJe^{\mathsf T}\). Its nontrivial logical operators are \(\ker(HJ)\setminus\operatorname{im}(H^{\mathsf T})\). Perfection means distinct radius-one error syndromes exhaust the syndrome space.

A *coordinatewise-collinear* matrix means that for every position \(i\) the \(r\)-vectors \(x_i=(H_X)_{\ast i}\) and \(z_i=(H_Z)_{\ast i}\) are proportional. No locality, LDPC, fault-tolerance, high Hamming distance, or computational decoding guarantee is asserted.

## Proof

**Construction.** For each one-dimensional subspace \(L\le\mathbb F_p^r\), choose its unique representative \(v_L\) whose first nonzero entry is \(1\). There are \((p^r-1)/(p-1)\) such lines. Since \(p\equiv1\pmod4\), the number \(m=(p-1)/2\) is even. The scalars \(1,2,\ldots,m\) select one vector from each antipodal pair of nonzero scalars. Partition these scalars into consecutive pairs
\[
(1,2),(3,4),\ldots,(m-1,m).
\]
For every line \(L\) and pair \((a,b)\), introduce one coordinate with \(x_i=a v_L\) and \(z_i=b v_L\). The number of coordinates is \((p^r-1)/4\). Let \(H=(H_X\mid H_Z)\), with these as its columns.

**Commutativity and rank.** For each coordinate, \(x_i z_i^{\mathsf T}-z_i x_i^{\mathsf T}=ab(v_Lv_L^{\mathsf T}-v_Lv_L^{\mathsf T})=0\), so \(HJH^{\mathsf T}=0\) term-by-term. As the set of \(x_i\)'s contains a nonzero representative of every projective line, these columns span \(\mathbb F_p^r\); hence \(\operatorname{rank}H=r\). The stabilizer therefore has size \(p^r\) and encodes \(n-r\) logical \(p\)-level qudits.

**Exhaustive one-error syndromes.** The syndromes of the four joint-Lee weight-one errors \(X_i^{\pm1},Z_i^{\pm1}\) are respectively \(\mp z_i\) and \(\pm x_i\). For a fixed line \(L\), the scalar pairs use \(\pm a v_L,\pm b v_L\) once each over the \((p-1)/4\) coordinates on that line. These exhaust \(L\setminus\{0\}\) without repetition. Distinct projective lines meet only at zero. Therefore the \(4n=p^r-1\) nonidentity radius-one errors have *all distinct nonzero* syndromes, with the identity having syndrome zero. The code is nondegenerate to this radius and saturates \(p^{n-r}(4n+1)=p^n\). Moreover, no nonzero Pauli error of joint-Lee weight at most two lies in \(\ker(HJ)\): any such error is the difference of two distinct radius-one errors, whose syndromes would otherwise coincide. Consequently \(d_{\diamond}\ge3\).

**An exact weight-three logical.** On any coordinate formed from \((a,b)=(1,2)\), let \(e=X_i Z_i^2\). Its syndrome is \(2x_i-z_i=0\) and its joint Lee weight is \(1+2=3\) for \(p\ge5\). To see that \(e\) is not a stabilizer, note that all columns on coordinates other than \(i\) still span \(\mathbb F_p^r\). Indeed, deleting one coordinate removes at most the one projective line of \(i\), whereas the other \((p^r-1)/(p-1)-1\) lines cannot lie in a hyperplane: a hyperplane contains only \((p^{r-1}-1)/(p-1)\) lines and the difference is \(p^{r-1}-1>0\). If \(e\in\operatorname{im}(H^{\mathsf T})\), a nonzero row combination of \(H\) would vanish on all these remaining spanning columns, impossible. Thus \(e\) is a nontrivial logical of weight three, proving \(d_{\diamond}=3\).

**Necessity within the collinear class.** Let an arbitrary prime-field perfect radius-one check matrix have collinear column pairs. Its error syndromes cover each nonzero vector exactly once. Every nonzero syndrome on a projective line \(L\) can only arise from coordinates whose two check columns lie on \(L\): all such columns must be nonzero, for a zero column would yield a zero syndrome. Each such coordinate contributes exactly two *distinct opposite-sign pairs* of nonzero vectors in \(L\) (the \(X\)- and \(Z\)-syndrome pairs); otherwise syndrome injectivity fails. Because \(L\setminus\{0\}\) has \((p-1)/2\) opposite-sign pairs, that number must be even. Therefore \(p\equiv1\pmod4\). This completes the claimed restricted-class congruence classification.

## Verification

The accompanying standalone standard-library program `verify.py` constructs the normalized projective lines, check matrices, and complete radius-one syndrome tables and verifies matrix rank, commutativity, distinctness, the weight-three zero-syndrome witness, and its non-stabilizer status. Exact tests pass at \((p,r)=(5,2),(5,3),(5,4),(13,2),(17,2)\). These are corroborating finite tests, not the proof for all parameters. Run `python3 verify.py` and compare its terminal line with the supplied `verification-output.txt`.

For an explicit six-coordinate example at \(p=5,r=2\), the construction gives
\[
H_X=\begin{pmatrix}0&1&1&1&1&1\\1&0&1&2&3&4\end{pmatrix},\qquad H_Z=2H_X\pmod5.
\]
The two check generators commute; the \(25\) possible zero-or-single-shift errors have \(25\) distinct syndromes. At \(p=5,r=3\), there are \(31\) coordinates and \(125\) syndromes. At \(p=13,r=2\), there are \(42\) coordinates and \(169\) syndromes.

## Relationship to prior work

Guo, Han, Chakraborty, Jain, Liu, Albert, and Lucas (2026), arXiv:2610.04834v1, Sections 3.1 and 4.3, introduce the joint/separate quantum Lee metrics and sphere-packing conventions. Their Table 2 lists a perfect six-qudit joint-Lee code on \(\mathbb Z_5\), a separate two-qudit joint-Lee family, and perfect *separate*-Lee CSS families, but does not give the present variable-rank projectively paired joint-Lee family. The construction above agrees with their radius-one cardinality \(1+4n\), but the proof of rowwise commutativity through pairing antipodal projective orbits is additional.

Matsumoto (2021), arXiv:2105.12354, treats Lee weights and constructions for CSS codes with independently protected shift/phase components. Its results do not directly imply the present non-CSS joint-Lee perfect-syndrome construction. Classical radius-one Lee codes and ordinary projective Hamming parity checks provide the underlying full-syndrome ingredient, but they do not on their own impose the symplectic isotropy required of an \(n\)-qudit stabilizer. The novelty asserted here is specifically the *coordinatewise-collinear symplectic pairing* and resulting all-rank family with its restricted-class parity obstruction, not projective syndrome counting or the pre-existing six-qudit parameters.

## Limitations

The construction requires primes \(p\equiv1\pmod4\). The obstruction for other odd primes applies **only** when the two check columns on every coordinate are collinear; noncollinear matrices may exist. These are joint-Lee codes for a fixed local Pauli frame, not ordinary Hamming-distance-three quantum codes. The stabilizer checks can be dense and no efficient fault-tolerant syndrome circuit is provided. The first small parameter member is already present at the level of parameters in the 2026 preprint; no inequivalence is claimed. Although targeted comparisons found no published theorem implying this entire family, priority relative to unpublished or unindexed symplectic constructions is not independently certified.

## References

1. J. Guo, Y. Han, A. Chakraborty, S. P. Jain, T. Liu, V. V. Albert, and A. Lucas, *Quantum codes in the Lee metric*, arXiv:2610.04834v1, first publicly submitted 2026-10-04. https://arxiv.org/html/2610.04834v1
2. R. Matsumoto, *Lee Weight for Nonbinary Quantum Error Correction*, arXiv:2105.12354, 2021. https://arxiv.org/abs/2105.12354
3. S. W. Golomb and L. R. Welch, *Perfect codes in the Lee metric and the packing of polyominoes*, SIAM Journal on Applied Mathematics 18 (1970), 302–317. Cited for classical Lee-code context; the complete original article was not inspected in this review.
