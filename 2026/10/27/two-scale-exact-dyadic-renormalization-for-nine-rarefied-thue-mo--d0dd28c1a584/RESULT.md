# Two-scale exact dyadic renormalization for nine-rarefied Thue–Morse sums

## Finding

For a nonnegative integer \(n\), write \(s_2(n)\) for the number of ones in its binary expansion and \(\epsilon(n)=(-1)^{s_2(n)}\). For every integer \(k\geq 0\) and \(j\in\{0,\ldots,8\}\), set
\[
F_j(k)=\sum_{0\leq i<2^k}\epsilon(9i+j).
\]
For \(k\geq1\), every integer \(m\geq0\), and each \(j\in\{0,\ldots,8\}\), one has the simultaneous exact law
\[
\boxed{F_j(k+6m)=3^mF_j(k)+\frac{27^m-3^m}{3}\bigl(F_j(k)+F_{j+3\,\bmod9}(k)+F_{j+6\,\bmod9}(k)\bigr).}
\]
Consequently \(F_j(k+12)=30F_j(k+6)-81F_j(k)\) for all \(k\geq1\). The order-two recurrence in blocks of six is minimal for the whole nine-coordinate vector: both characteristic factors \(3\) and \(27\) occur nontrivially at \(k=1\). This is an exact two-scale (rather than a merely asymptotic) decomposition.

## Assumptions and scope

The indices \(j\) range over all nine residues, the dyadic exponent \(k\) is any integer at least one, and the block count \(m\) is any nonnegative integer. Residues appearing as subscripts are interpreted modulo nine, taking representatives \(0\) through \(8\). The scalar recurrence is not claimed to be minimal for each individual fixed residue and fixed starting phase. No assertion concerns arbitrary nondyadic cutoffs.

## Proof

Let \(V(k)=(F_0(k),\ldots,F_8(k))^{\mathsf T}\). The binary digit law \(\epsilon(2u+r)=(-1)^r\epsilon(u)\) for \(r\in\{0,1\}\) implies that the decomposition \(i=2a+r\) yields
\[
F_j(k+1)=\sum_{r=0}^1(-1)^{(9r+j)\bmod2}\,F_{\lfloor(9r+j)/2\rfloor}(k).
\]
The quotient is always in \(\{0,\ldots,8\}\). Thus \(V(k+1)=BV(k)\), where the nine rows of the integral matrix \(B\), in zero-based coordinates, are
\[
\begin{pmatrix}
1&0&0&0&-1&0&0&0&0\\
-1&0&0&0&0&1&0&0&0\\
0&1&0&0&0&-1&0&0&0\\
0&-1&0&0&0&0&1&0&0\\
0&0&1&0&0&0&-1&0&0\\
0&0&-1&0&0&0&0&1&0\\
0&0&0&1&0&0&0&-1&0\\
0&0&0&-1&0&0&0&0&1\\
0&0&0&0&1&0&0&0&-1
\end{pmatrix}.
\]
A finite, exact multiplication (also reproduced in the standalone verifier) establishes
\[
B^6=3I+8Q-3J,
\]
where \(J\) is the all-ones matrix and \(Q_{jh}=1\) exactly when \(j\equiv h\pmod3\), otherwise zero. This is a completely explicit nine-by-nine identity; in particular its entries are \(8\) on the diagonal, \(5\) at distinct indices congruent modulo three, and \(-3\) otherwise.

For \(k\geq1\), summing over \(j\) gives
\[
\sum_{j=0}^8F_j(k)=\sum_{n=0}^{9\cdot2^k-1}\epsilon(n)=0,
\]
because the terms \(\epsilon(2a)\) and \(\epsilon(2a+1)\) cancel in pairs. Hence \(JV(k)=0\). Moreover \(Q^2=3Q\). Setting \(P=Q/3\), the matrix \(P\) is an idempotent and
\[
V(k+6)=(3I+24P)V(k)=3(I-P)V(k)+27PV(k).
\]
The two summands are eigencomponents, so for every \(m\geq0\),
\[
V(k+6m)=3^m(I-P)V(k)+27^mPV(k).
\]
Expanding coordinate \(j\) proves the displayed exact formula. Both eigencomponents are necessary: from the direct calculation
\[
V(1)=(2,0,-2,2,-2,0,2,-2,0)^{\mathsf T},
\]
one has \((QV(1))_0=6\ne0\), and \((3V(1)-QV(1))_1=4\ne0\). The eigenvalues \(3\) and \(27\) are distinct, so no first-order scalar recurrence in six-step time can describe the whole vector beginning at \(k=1\). The second-order relation is therefore minimal. This argument establishes the result for all requested indices without numerical extrapolation.

## Verification

The standalone `verify.py` constructs \(B\) independently from binary digit carries, multiplies it six times with integer arithmetic, checks \(B^6=3I+8Q-3J\) and \(Q^2=3Q\), evaluates the defining sums directly for \(1\leq k\leq13\), and cross-checks the exact law for \(1\leq k\leq18\) and \(0\leq m\leq3\). It confirms the nonzero components at \(k=1\). These finite checks certify the nonstandard finite matrix identity and illustrate the definitions; the infinite quantifiers follow from the algebraic proof above.

## Relationship to prior work

J. Shallit's 2023 paper studies \(f_{b,j}(N)=\sum_{i<N}\epsilon(bi+j)\), giving automaton-based results for \(b=3\) and \(b=5\), and discussing \(b=7\). Its full accessible preprint does not state this nine-residue two-scale exact identity. Older studies by Goldstein–Kelly–Speer concern scaling for odd prime moduli, whereas the theorem above is for the first odd composite prime-square modulus, nine. Drmota–Skałba examine rarefied sums for arbitrary odd moduli, including positivity when the modulus is divisible by three; their accessible abstract does not establish this exact all-shifts dyadic formula, but their full text could not be checked and is a substantive originality risk. The result is a specific, exact composite-modulus refinement of the literature's scaling theme, not a claim to invent the transfer-matrix technique.

## Limitations

This theorem determines only dyadic prefix lengths and modulus nine. It does not characterize all signs for arbitrary cutoffs, nor extend directly to all composite moduli. Publication priority remains unverified; full-text comparison with two older potentially relevant articles was unavailable.

## References

1. J. Shallit, *Rarefied Thue-Morse Sums Via Automata Theory and Logic*, public preprint February 18, 2023, arXiv:2302.09436; https://arxiv.org/html/2302.09436v2 (full text examined, especially Section 6).
2. S. Goldstein, K. Kelly, and E. R. Speer, *The fractal structure of rarefied sums of the Thue-Morse sequence*, Journal of Number Theory 42 (1992), 1–19. DOI:10.1016/0022-314X(92)90104-W (abstract available).
3. M. Drmota and M. Skałba, *Rarified sums of the Thue-Morse sequence*, Transactions of the American Mathematical Society 352 (2000), 609–642. DOI:10.1090/S0002-9947-99-02277-1 (abstract available).
