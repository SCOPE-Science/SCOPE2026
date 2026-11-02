# Two shift-commuting conjugacy classes among three unresolved binary two-to-one cellular automata

## Finding

Let \(X=\mathbb F_2^{\mathbb Z}\) be the two-sided binary full shift, with the product topology. For \(x\in X\), every subscript is an integer. Work over \(\mathbb F_2\), so addition means exclusive-or. Define three cellular automata \(A,B,C:X\to X\) using their consecutive five-site input \((a,b,c,d,e)=(x_i,x_{i+1},x_{i+2},x_{i+3},x_{i+4})\):

\[
\begin{aligned}
 A(x)_i&=b+c+(a+b)(cd+(c+d+1)e),\\
 B(x)_i&=b+c+a(c+1)d+b(d+1)e,\\
 C(x)_i&=b+(a+b)(cd+ce+c+de)+c(d+e)+de.
\end{aligned}
\]

These are precisely the three non-bipermutive, two-to-one five-site representatives whose locally-eventually-onto status is left unknown in Appendix B of Haugland--Larsen--Omland--Rustad (2026). **Among these three actual representatives, there are exactly two classes under shift-commuting topological conjugacy:** \(A\) and \(B\) are conjugate by an explicit invertible cellular automaton, while \(C\) is conjugate to neither.

More precisely, define the difference cellular automaton \(D:X\to X\) and the four-site reversible cellular automaton \(P:X\to X\) by

\[
D(x)_i=x_i+x_{i+1},\qquad P(x)_i=x_{i+1}+x_i(1+x_{i+2})x_{i+3}.
\]

Then the exact identities on all of \(X\) are

\[
\boxed{A=P\circ D,\qquad B=D\circ P,\qquad A\circ P=P\circ B.}
\]

The conjugacy \(P\) has inverse

\[
\boxed{P^{-1}(y)_i=y_{i-1}+y_{i-2}(1+y_i)y_{i+1}.}
\]

For the spatial period-five subspace \(X_5=\{x\in X:x_{i+5}=x_i\ \forall i\}\), the distinguishing invariant is

\[
\boxed{\left|\operatorname{Fix}_{X_5}(A^5)\right|=\left|\operatorname{Fix}_{X_5}(B^5)\right|=1,\quad
\left|\operatorname{Fix}_{X_5}(C^5)\right|=6.}
\]

As a consequence, \(A\) is locally eventually onto if and only if \(B\) is; the three representative decisions reduce to at most two independent questions. **The LEO status of neither remaining class is established here.**

## Assumptions and scope

All configurations are bi-infinite binary sequences, not finite words with fixed boundary conditions. A topological conjugacy of \((X,F)\) and \((X,G)\) means a homeomorphism \(H:X\to X\) such that \(H\circ F=G\circ H\); here \(H=P\) also commutes with spatial shift. \(F^5\) denotes five temporal iterations, while \(X_5\) imposes five-site *spatial* periodicity. \(X_5\) contains exactly \(2^5=32\) configurations. The statement classifies the three displayed representatives; it does not assert a classification of their entire elementary-equivalence families under every possible normalization.

## Proof

**1. Factorization and conjugacy.** Expanding \(P(Dx)_i\) gives

\[
(x_{i+1}+x_{i+2})+(x_i+x_{i+1})(1+x_{i+2}+x_{i+3})(x_{i+3}+x_{i+4}).
\]

For binary variables \(c,d,e\), the Boolean identity

\[
(1+c+d)(d+e)=cd+(c+d+1)e
\]

reduces this expression exactly to \(A(x)_i\). Similarly,

\[
(D(Px))_i=P(x)_i+P(x)_{i+1}
=b+c+a(c+1)d+b(d+1)e=B(x)_i.
\]

Both identities are local five-bit identities and therefore hold for every bi-infinite configuration. The displayed \(P^{-1}\) is a two-sided inverse. In fact, substituting the local rules into \(P^{-1}P\) and \(PP^{-1}\) gives the identity in \(\mathbb F_2\) for all seven-bit neighborhoods. This finite Boolean identity can be checked exhaustively by the 128-case section of `verify.py`; seven sites cover *every* variable on which either composition depends. Consequently the compositions equal the identity on the full shift, not merely on a sampled collection of finite rings. As an alternative source, reversibility of this four-bit local rule was established earlier by Haugland and Omland (2024, Example 1.3).

It follows that \(P\) is a shift-commuting homeomorphism and

\[
A\circ P=(P\circ D)\circ P=P\circ(D\circ P)=P\circ B.
\]

Thus \(B=P^{-1}AP\), proving the conjugacy.

**2. A periodic-point obstruction.** Each automaton preserves \(X_5\) because it commutes with shift. Identify \(X_5\) with binary five-tuples, applying each displayed local rule at the five cyclic indices. Complete enumeration of the 32 inputs gives the following temporal periodic orbits (transient configurations are omitted):

\[
\begin{array}{c|c|c|c}
\text{rule}&\text{temporal cycle lengths on }X_5&\text{periodic states}&|\operatorname{Fix}_{X_5}(F^5)|\\\hline
A&1,10&11&1\\
B&1,10&11&1\\
C&1,5&6&6
\end{array}
\]

In all three rows, \(00000\) is the unique fixed state. For \(C\), the other recurrent cycle is explicitly

\[
00001\to00010\to00100\to01000\to10000\to00001.
\]

In contrast, for \(A\) and \(B\) the other periodic orbit has length ten, which does not divide five. Every one of the 32 transitions for each rule, including the absence of any omitted cycles, is independently reconstructed and exhaustively checked by `verify.py`; the algorithm starts at each as-yet-unvisited vertex of the complete 32-vertex functional graph and records each directed cycle. This is a finite exhaustive proof of the displayed counts.

If a shift-commuting conjugacy \(H\) between \(C\) and \(A\) or \(B\) existed, then \(H(X_5)=X_5\), because \(H\sigma^5=\sigma^5H\) and likewise for its inverse. Also \(H\) would biject their sets of fixed points of fifth temporal iterates. The counts six and one differ, a contradiction. Therefore \(C\) is in a separate conjugacy class among the three.

**3. LEO consequence.** If \(F=HGH^{-1}\) with \(H\) a homeomorphism, then \(F^m(H(U))=H(G^m(U))\) for every open set \(U\) and every integer \(m\ge0\). The condition that each nonempty open set eventually maps onto \(X\) is therefore conjugacy invariant. Hence \(A\) and \(B\) have identical LEO status. Their unknown statuses are not determined by the conjugacy.

## Verification

The standalone Python 3 standard-library program `verify.py` checks all 32 possible five-bit local inputs for the two factorizations \(A=PD\) and \(B=DP\); all 128 possible seven-bit contexts for both directions of the inverse identity for \(P\); every cyclic input up through length eight; and every transition on \(X_5\), yielding temporal cycle types \([1,10]\), \([1,10]\), \([1,5]\). It produces `VERIFY_OK` after every assertion passes. To reproduce: run `python3 verify.py` with Python 3.8 or newer. The exhaustive finite computations prove exactly the local identities and the complete 32-state graph census used above; they are not used as a replacement for the all-configuration factorization and conjugacy arguments.

## Relationship to prior work

Haugland, Larsen, Omland and Rustad (2026, Appendix B, page 27, first three question-mark entries of their table) enumerate these three binary non-bipermutive two-to-one rules and explicitly leave their LEO status unresolved. Their enumeration and the two-to-one property are credited, not claimed as new. Haugland and Omland (2024, Example 1.3) identify the same four-bit reversible rule \(P\). The contribution here is to detect the precise \(PD/DP\) conjugate pair, distinguish the third representative by a minimal small-ring temporal signature, and reduce the number of potentially independent LEO decisions. The identity by itself would not establish the negative comparison for the third rule; that comparison uses the complete five-site periodic graph.

## Limitations

No LEO conjecture is solved, and neither an LEO-positive nor an LEO-negative result is claimed for the unresolved examples. The classification concerns the given three representative local formulas on the bi-infinite shift; the periodic-obstruction proof does not assert that arbitrary homeomorphic conjugacy lacking shift commutation is impossible. It also does not classify all finite-to-one binary cellular automata or quantify mixing rates. The 2026 paper may have additional unpublished equivalences or later work; publication priority has not been independently certified.

## References

1. J. K. Haugland, N. S. Larsen, T. Omland, H. G. Rustad, *Locally eventually onto cellular automata*, arXiv:2610.33131v1, first public posting 2026-10-23. Appendix B, p. 27. https://arxiv.org/abs/2610.33131
2. J. K. Haugland, T. Omland, *New classes of reversible cellular automata*, arXiv:2411.00721v1, first public posting 2024-11-01. Example 1.3 and Proposition 1.4. https://arxiv.org/abs/2411.00721
