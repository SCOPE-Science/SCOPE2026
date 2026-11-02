# An exact \(13/280\) periodic obstruction for six-term Zeckendorf–Niven runs

## Finding
Let \(F_0=0\), \(F_1=1\), and \(F_{j+2}=F_{j+1}+F_j\). Write \(s_Z(n)\) for the number of nonadjacent Fibonacci terms in the canonical Zeckendorf representation of a positive integer \(n\). An integer is Zeckendorf–Niven if \(s_Z(n)\) divides \(n\).

**Theorem.** If \(n\ge21\) and all six integers \(n,n+2,n+4,n+6,n+8,n+10\) are Zeckendorf–Niven, then \(n=F_G-3\) or \(n=F_G-5\) for some \(G\ge21\). In the first case \(G\) belongs to an explicitly computed set of **33 even residue classes** modulo \(1680\). In the second case \(G\) belongs to an explicitly computed set of **45 odd residue classes**, disjoint from the first set. Therefore the union of *locally admissible index classes* has cardinality \(78\), giving the exact local-sieve fraction \(78/1680=13/280\).

The first two prime cutoffs in the same increasing small-prime sieve leave respectively \(210/1680=1/8\) (primes at most \(3\)) and \(112/1680=1/15\) (primes at most \(5\)). Adding \(7\) is the first of these consecutive prime thresholds for which fewer than five percent of Fibonacci indices remain locally admissible. The theorem **does not assert** that a surviving residue class actually contains a six-term run.

## Assumptions and scope
The prior two-shape reduction, which identifies \(n+3\) or \(n+5\) as a Fibonacci number for any six-term run beginning at \(n\ge21\), is taken as the established source theorem [2]. The new work concerns the precise arithmetic obstruction on the Fibonacci index; its input is a necessary condition, not an equivalence with a six-term run. The source theorem and the two Zeckendorf-weight profiles below apply to ordinary positive integers and the standard Fibonacci normalization.

## Proof
The source's gap-reduction theorem [2] states that a six-term run outside the small initial block must have \(n=F_G-3\) or \(n=F_G-5\), for \(G\ge21\). The associated exact six-shift Zeckendorf-weight profiles, also obtainable by peeling two Fibonacci indices, are
\[
(s_Z(F_G-3+2j))_{j=0}^{5}=(r,r+1,2,2,2,3),\quad r=\lfloor(G-1)/2\rfloor,
\]
and (the second form occurs only for odd \(G\))
\[
(s_Z(F_G-5+2j))_{j=0}^{5}=(r-1,r,r+1,2,2,2),\quad r=(G-1)/2.
\]
These identities can be checked at each parity base index using the canonical nonadjacency decomposition and transported by \(s_Z(F_{G+2}-w)=s_Z(F_G-w)+1\) for the fixed small positive offsets \(w\) in question.

Put \(V=F_G\). For the first shape, divisibility of the six terms forces
\[
r\mid V-3,\quad r+1\mid V-1,\quad 2\mid V+1,\quad 3\mid V+7.
\]
For the second shape, necessarily \(G\) is odd and
\[
r-1\mid V-5,\quad r\mid V-3,\quad r+1\mid V-1,\quad 2\mid V+1.
\]
The duplicated mod-two tests are redundant. In particular, both shapes require \(V\) odd, hence \(3\nmid G\) because the Fibonacci sequence is even precisely at indices divisible by \(3\). The first shape additionally requires \(V\equiv2\pmod3\).

For a prime \(p\), a necessary consequence of \(d\mid V-c\) is
\[
p\mid d\quad\Longrightarrow\quad F_G\equiv c\pmod p.
\]
Apply this implication to the displayed denominators and targets for each \(p\in\{2,3,5,7\}\), along with the parity and mod-three requirements. The Fibonacci sequences modulo \(2,3,5,7\) have respective periods \(3,8,20,16\). Because each denominator is an affine expression in \(\lfloor G/2\rfloor\), divisibility of those denominators by \(p\) is determined by \(G\bmod2p\). Therefore every condition is periodic in \(G\) with period dividing
\[
\operatorname{lcm}(\operatorname{lcm}(4,3),\operatorname{lcm}(6,8),\operatorname{lcm}(10,20),\operatorname{lcm}(14,16))=1680.
\]
The accompanying exact arithmetic verifier evaluates a full period of \(1680\) indices for each shape. At cutoffs \(3,5,7\) the union sizes are exactly \(210,112,78\), respectively. At cutoff \(7\), the first shape contributes \(33\) even classes and the second \(45\) odd classes, so they are disjoint. Periodicity makes this a proof for every \(G\ge21\), not merely a finite test of large Fibonacci indices. The ultimate fraction is \(78/1680=13/280\), as claimed.

## Verification
Run `python3 verify.py` in the same folder. It computes all Fibonacci residues by integer recurrence, independently tests their period invariance, and enumerates the complete local divisibility filter twice on adjacent index periods. It asserts the exact size triplet \(210,112,78\), the refined counts \(33,45\), disjointness, and the period \(1680\). The finite enumeration is exhaustive **of the periodic necessary-condition problem**; it is not an exhaustive enumeration of all original integers \(n\).

## Relationship to prior work
Lao, Miller, Rosa, Shiliaev, Tresch, Wong and Zhang [1] introduce the six-term gap between their infinite five-term construction and the known eight-term bound. A subsequent publicly posted study [2] supplies the unbounded two-Fibonacci-shape reduction and a finite exclusion through Fibonacci index \(501\). This theorem uses that reduction but adds a separate **infinite-index periodic characterization of the first-prime local obstruction**, with exact small-prime frontier \(1/8,1/15,13/280\). It does not claim the source's structural reduction or finite exclusion as new; nor is the present local congruence filter a proof that six-term runs never occur.

## Limitations
The \(78\) classes satisfy **only the specified local prime-divisor congruences**. Large prime factors of the index-dependent denominators can still exclude them, and none is asserted to give an actual six-term run. The source [2] is accessible in indexed scientific summaries, but its complete paper was not obtained in this examination, leaving residual priority uncertainty about unindexed supplementary congruence calculations. Its already reported shape theorem is used as a mathematical premise. The present result makes no distribution claim about actual runs and does not settle the open maximum-length question.

## References
[1] K. Lao et al., “On Zeckendorf-Niven numbers and arithmetic progressions,” arXiv:2606.24006v1 (first public 2026-06-22), https://arxiv.org/abs/2606.24006.

[2] “Consecutive Zeckendorf–Niven terms in a \(2\)-AP: a two-parameter family of five-term runs, and six-term runs confined to two Fibonacci shapes,” indexed public research manuscript, https://lean.up.railway.app/ (see its ZA4 and ZA5 descriptions); complete document unavailable for inspection here.
