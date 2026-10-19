# Forbidden nilpotency indices and length-independent extremal density in \(2\times2\) chain-ring matrices

## Finding
Let \(R\) be an arbitrary finite commutative chain ring of length \(m\ge3\), with maximal ideal \((\pi)\), residue field of size \(q\), and \(\pi^m=0\ne\pi^{m-1}\). For each nilpotent \(A\in M_2(R)\), write \(\nu(A)\) for the least positive integer \(h\) with \(A^h=0\). Then
\[
\nu(A)\in\{1,2,\ldots,m+1\}\cup\{2m\}.
\]
Both boundary indices \(m+1\) and \(2m\) occur. In particular, **every index from \(m+2\) to \(2m-1\) is absent**, and this forbidden interval grows linearly with ring length.

There are exactly \(q^{4m-2}\) nilpotent matrices in \(M_2(R)\). Of these, exactly
\[
(q^2-1)(q-1)q^{4m-5}
\]
have the extremal index \(2m\). Thus the extremal density among all nilpotent matrices is
\[
\frac{(q^2-1)(q-1)}{q^3},
\]
independent of \(m\), the characteristic, and the isomorphism type of the chain ring.

The chain hypothesis is a genuine boundary: over \(S=k[x,y]/(x^2,y^2)\) with \(\operatorname{char}k\ne2\), the radical also has nilpotency length three, but the matrix
\[
C=\begin{pmatrix}0&-x\\1&y\end{pmatrix}
\]
has \(\nu(C)=5\), an index impossible for length-three chain rings. Over characteristic two, this same matrix has index four.

## Assumptions and scope
A *finite commutative chain ring of length* \(m\) is a finite unital commutative local ring whose ideals are \(R\supset(\pi)\supset\cdots\supset(\pi^{m-1})\supset(0)\), all inclusions strict. The residue cardinality is \(q=|R/(\pi)|\). Consequently \(|R|=q^m\), \(|(\pi)^i|=q^{m-i}\), and \((\pi)^m=(0)\). No equal-characteristic or splitting assumption is imposed. Nilpotent means a positive power is literally the zero matrix over \(R\), not merely that its reduction is nilpotent.

## Proof
**Reduction and cyclicity.** Denote reduction modulo \(\pi\) by a bar. If \(A\) is nilpotent, then \(\bar A\) is nilpotent. Conversely, if \(\bar A\) is nilpotent then \(\bar A^2=0\), so \(A^2\in\pi M_2(R)\), whence \(A^{2m}=0\). The number of nilpotent matrices over \(\mathbb F_q\) of size two is exactly \(q^2\): the zero matrix and \(q^2-1\) nonzero rank-one nilpotents. One way to see the latter number is to choose a line \(L\) (\(q+1\) choices) and a nonzero map \(\mathbb F_q^2/L\to L\) (\(q-1\) choices). Therefore the total number of nilpotent lifts is \(q^2 q^{4(m-1)}=q^{4m-2}\).

If \(\bar A=0\), then \(A\in\pi M_2(R)\), hence \(A^m=0\). Otherwise \(\bar A\) is a single nilpotent Jordan block. It is cyclic, and a cyclic vector lifts by Nakayama's lemma. Thus \(I,A\) are linearly independent over \(R\) and \(A\) is similar to the companion matrix of \(X^2-tX+d\), where \(t=\operatorname{tr}(A)\in(\pi)\) and \(d=\det(A)\in(\pi)\). Cayley–Hamilton gives \(A^2=tA-dI\).

**Power recurrence.** Write \(A^h=u_hA+v_hI\), where \(u_0=0\), \(u_1=1\), and for positive \(h\) put \(v_h=-d u_{h-1}\). Then
\[
u_{h+1}=t u_h-d u_{h-1},\qquad
u_h=\sum_{j=0}^{\lfloor(h-1)/2\rfloor}(-1)^j\binom{h-1-j}{j}t^{h-1-2j}d^j.
\]
These coefficients are unique because \(I,A\) are linearly independent. The formulas follow by induction from Cayley–Hamilton and are valid in every characteristic, since binomial coefficients act by repeated addition in \(R\).

If \(d\in(\pi^2)\), every summand of \(u_h\) belongs to \((\pi^{h-1})\). Thus \(u_{m+1}=0\), and \(v_{m+1}=-d u_m=0\); consequently \(A^{m+1}=0\).

If \(d\in(\pi)\setminus(\pi^2)\), then in the formula for \(u_{2m-1}\) the unique term with valuation below \(m\) is \((-d)^{m-1}\), while \(v_{2m-1}=-du_{2m-2}=0\). Hence
\[
A^{2m-1}=(-d)^{m-1}A\ne0,
\]
because \(d^{m-1}\ne0\) and \(A\bmod\pi\ne0\). Every term of \(u_{2m}\) lies in \((\pi^m)\), and \(v_{2m}=0\), so \(A^{2m}=0\). This proves the claimed dichotomy.

**Extremal count.** For each of the \(q^2-1\) nonzero nilpotent residue matrices \(N\), there are \(q^{4(m-1)}\) lifts. The determinant has nonzero gradient at \(N\), because a rank-one matrix has a nonzero cofactor. Accordingly its coefficient in \(\pi/\pi^2\) is a nonzero affine-linear functional of the four first-order lift coordinates. Exactly a fraction \((q-1)/q\) of lifts satisfy \(d\in(\pi)\setminus(\pi^2)\). The exact number having index \(2m\) is therefore \((q^2-1)q^{4(m-1)}(q-1)/q\). Division by the total \(q^{4m-2}\) proves the density.

**Sharpness and non-chain boundary.** The companion matrix for \(X^2-\pi X\) has \(A^h=\pi^{h-1}A\) for \(h\ge1\), and so has index \(m+1\). The companion matrix for \(X^2+\pi\) has index \(2m\). Over \(S=k[x,y]/(x^2,y^2)\), Cayley–Hamilton for the displayed \(C\) gives \(C^2=yC-xI\), and hence
\[
C^4=-2xyC,\qquad C^5=0.
\]
Since \(xy\ne0\), the first identity makes \(C^4\ne0\) if \(\operatorname{char}k\ne2\). In characteristic two, \(C^4=0\) but \(C^3=-xC-xyI\ne0\), so the index is four. This establishes the stated sharp boundary.

## Verification
The standalone file `verify_nilpotent_gap.py` uses literal matrix multiplication, not a recurrence or the claimed counting formula, to enumerate all nilpotent matrices over \(\mathbb Z/8\mathbb Z\), \(\mathbb F_2[t]/(t^3)\), \(\mathbb Z/16\mathbb Z\), and \(\mathbb Z/27\mathbb Z\). It checks the gap, the exact extremal count, and the complete index histograms; the two length-three rings with \(q=2\) yield the same histogram. It also checks the displayed non-chain witness in characteristics two, three, and five. Run with `python3 verify_nilpotent_gap.py`. Exhaustive finite computations are checks, not a substitute for the proof for arbitrary length and residue size.

## Relationship to prior work
Avni, Onn, Prasad and Vaserstein (2007/2008), Section 2, give a general cyclic-companion normal form for two-by-two matrices over local principal ideal rings; that normal form, rather than a new similarity classification, is used here. Their Section 2.2 enumerates similarity classes, not the support of nilpotency indices or the extremal-index matrix mass. Prasad, Singla and Spallone (2012), Section 6.2, treat nilpotent lifts over length-two local rings. A separately published exact calculation for lifts of a single nilpotent Jordan block over \(\mathbb F_q[\varepsilon]/(\varepsilon^3)\) gives an important length-three, equal-characteristic antecedent. The present statement concerns every finite commutative chain ring at **all lengths \(m\ge3\)**, shows an unbounded forbidden interval, gives the length-independent global nilpotent density, and identifies a non-chain boundary. The result does not assert that cyclic normal forms, Cayley–Hamilton, or the length-three lift calculation are new.

## Limitations
This does not give every lower-index multiplicity for arbitrary \(m\), nor does it extend the gap to all finite local rings. The non-chain witness concerns \(k[x,y]/(x^2,y^2)\), not every non-chain local ring. The novelty of this explicit power-index refinement relative to other literature may require further specialist checking: broad known similarity classifications could facilitate independent derivations of the same formulas.

## References
1. N. Avni, U. Onn, A. Prasad and L. Vaserstein, *Similarity classes of 3x3 matrices over a local principal ideal ring*, arXiv:0708.1608v1 (12 August 2007), Section 2 and Theorem 2.2, https://arxiv.org/abs/0708.1608.
2. A. Prasad, P. Singla and S. Spallone, *Similarity of matrices over local rings of length two*, arXiv:1212.6157v1 (26 December 2012), Section 6.2, https://arxiv.org/abs/1212.6157.
3. *Exact nilpotency-index distribution for Jordan lifts over finite dual numbers*, published mathematical research record (2026), studied as a limited-length antecedent by its public abstract.
