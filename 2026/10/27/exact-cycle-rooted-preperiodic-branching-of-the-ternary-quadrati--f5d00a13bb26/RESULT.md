# Exact cycle-rooted preperiodic branching of the ternary quadratic Chebyshev map

## Finding

Consider \(\displaystyle F_k(x)=x^2-2\pmod{3^k}\), for each integer \(k\ge1\), on the ring \(\mathbb Z/3^k\mathbb Z\). Every residue \(y\equiv2\pmod3\) is periodic, every residue \(z\equiv1\pmod3\) enters the periodic set after one step, and every residue \(x\equiv0\pmod3\) enters after exactly two steps. Thus each depth comprises \(3^{k-1}\) residues.

Every periodic residue \(y\) has exactly one depth-one predecessor \(z\equiv1\pmod3\). Define its **depth-two attachment number**
\[
b_k(y)=\#\{x\bmod3^k:x\equiv0\pmod3,\ F_k^{\,2}(x)=y\}.
\]
The full local branching law is
\[
b_k(2)=3^{\lfloor k/2\rfloor}.
\]
For \(y\equiv2\pmod3\) but \(y\not\equiv2\pmod{3^k}\), write
\[
s=\nu_3(y-2)\in\{1,\ldots,k-1\},\qquad
u=\frac{y-2}{3^s}\pmod3\in\{1,2\}.
\]
Then
\[
b_k(y)=
\begin{cases}
2\cdot3^{s/2},&s\text{ is even and }u=2,\\
0,&\text{otherwise}.
\end{cases}
\]

These attachment numbers are constant along each cycle. For each even integer \(s=2v\) with \(2\le s<k\), precisely **one** periodic cycle has attachment number \(2\cdot3^v\); this cycle has length \(3^{k-s-1}\). The fixed point \(y=2\) has attachment number \(3^{\lfloor k/2\rfloor}\). Every other periodic cycle has no depth-two attachments. In particular the rooted transient-tree shapes are highly nonuniform even though each periodic vertex has exactly one depth-one predecessor.

## Assumptions and scope

All residue classes, primes, valuations and counts refer to the specified finite ring and integer \(k\ge1\). A depth-one predecessor means a point outside the periodic set mapping directly into it. Depth-two predecessors are counted by their image after exactly two iterations; no assertion is made about preimages in a different dynamical system. For \(k=1\), the only periodic residue is \(2\), and the set of even valuations \(s<k\) is empty.

## Proof

**Periodic set and depth.** Reduction modulo \(3\) gives \(0\mapsto1\mapsto2\mapsto2\). On \(x\equiv2\pmod3\), the polynomial derivative \(F_k'(x)=2x\equiv1\pmod3\) is a unit. For every \(k\), Hensel lifting of the equation \(z^2-2=y\) from \(z\equiv2\pmod3\) provides a unique preimage on that residue class; thus the map is a permutation of the \(3^{k-1}\) residues \(2\pmod3\), and all are periodic. Likewise, for each \(y\equiv2\pmod3\) there is a unique \(z\equiv1\pmod3\) with \(F_k(z)=y\), since \(2z\equiv2\pmod3\) is a unit. The mod-\(3\) transitions force the stated exact depths.

**An exact quadratic preimage count.** For a depth-two point \(x\equiv0\pmod3\),
\[
F_k^2(x)=x^4-4x^2+2,\qquad
F_k^2(x)-2=x^2(x^2-4).
\]
Since \(x^2-4\equiv2\pmod3\), the valuation of the latter difference in integers is \(2\nu_3(x)\), and its first nonzero base-\(3\) digit is \(2\). This excludes every nonzero \(y-2\) having odd valuation or leading digit \(1\). If \(y=2\), the factor \(x^2-4\) is a unit, so \(F_k^2(x)=2\) exactly when \(3^{\lceil k/2\rceil}\mid x\); there are \(3^{\lfloor k/2\rfloor}\) such classes. Otherwise let \(s=2v<k\) and \(u=2\). Write \(x=3^v w\), \(3\nmid w\); the congruence reduces to
\[
w^2(3^{2v}w^2-4)\equiv(y-2)/3^{2v}\pmod{3^{k-2v}}.
\]
Modulo \(3\), this reads \(2w^2=2\), with roots \(w=1,2\). The derivative of the left polynomial is
\[
4w(3^{2v}w^2-2)\equiv w\pmod3,
\]
nonzero at both roots. Each lifts uniquely modulo \(3^{k-2v}\); since \(w\) ranges modulo \(3^{k-v}\), each gives \(3^v\) residue classes \(x\), proving \(b_k(y)=2\cdot3^v\).

**Cycle constancy.** On the periodic residue class \(y\equiv2\pmod3\),
\[
F_k(y)-2=(y-2)(y+2),\quad y+2\equiv1\pmod3.
\]
Hence the \(3\)-adic valuation of \(y-2\), truncated at \(k\), and its nonzero leading base-\(3\) digit are unchanged along forward orbits. The formula for \(b_k(y)\) is therefore constant along each cycle.

**Exactly one rich cycle at each even valuation.** Let \(2\le s<k\). There are \(3^{k-s-1}\) residues satisfying \(\nu_3(y-2)=s\) and \((y-2)/3^s\equiv2\pmod3\). To prove these form one cycle, let \(y\) be any of them and put \(\Delta=F_k(y)-y=(y-2)(y+1)\). Since \(s\ge2\), we have \(\nu_3(y+1)=1\), so \(m:=\nu_3(\Delta)=s+1\ge3\). Along this orbit the derivative is always \(1\pmod3\). For each iterate \(H=F_k^{3^j}\), if \(\nu_3(H(y)-y)=m+j\), Taylor expansion with integral coefficients and \(H'(y)\equiv1\pmod3\) gives
\[
H^3(y)-y \equiv (1+H'(y)+H'(y)^2)(H(y)-y)
\pmod{3^{2(m+j)}}.
\]
The coefficient \(1+H'(y)+H'(y)^2\) has valuation exactly one, and \(2(m+j)\ge m+j+2\); consequently the displacement valuation increases by exactly one. An iterate exponent not divisible by \(3\) does not raise the valuation, because its displacement is the first displacement times a unit modulo the next power of \(3\). Repeatedly stripping factors of \(3\) proves
\[
\nu_3(F^t(y)-y)=m+\nu_3(t)
\]
up to the precision \(k\). Therefore the least period modulo \(3^k\) is \(3^{\max(0,k-m)}=3^{k-s-1}\). The invariant set at the fixed valuation and leading digit has exactly the same cardinality and is thus a single cycle. Taking \(s\) even gives each asserted rich cycle; all other cycles have zero depth-two branching by the exact preimage formula. The point \(2\) is fixed and handled separately.

## Verification

The standalone exact-integer Python program `verify.py` independently enumerates the functional graph for moduli \(3^k\), \(1\le k\le8\), checks all depths, compares every depth-two fiber with the valuation formula, verifies constancy along each cycle, and confirms the one-cycle-per-even-valuation conclusion. These are corroborative finite tests; the proof above establishes the statements for every \(k\ge1\).

## Relationship to prior work

Chebyshev functional graphs over finite fields were treated by Gassert (2012); finite-field results do not classify degree-two preperiod-two fibers over the nonreduced rings \(\mathbb Z/3^k\mathbb Z\). The general fixed-point and exact-periodic-point formulas of Panraksa and Tangboonduangjit (2026) include this polynomial up to the invertible scaling \(x=2z\); our claim is instead a fiber-by-fiber **preperiodic attachment classification**, not a new formula for the number of cycles or periodic points. Lu, Dai and Li (2026) address Chebyshev **permutation** polynomials over ternary prime-power rings, whereas the degree-two map here is nonpermuting on the full ring.

## Limitations

This is the degree-two, \(3\)-power-modulus case; it does not classify arbitrary degrees, primes or composite moduli. The cycle lengths used in the proof are derived locally for the rich cycles, not asserted novel relative to all existing periodic-point literature. The existence of an equivalent unindexed description of the preperiodic tree fibers has not been ruled out by independent publication-priority audit.

## References

- T. Alden Gassert, *Chebyshev Action on Finite Fields*, arXiv:1209.4396 (first posted 2012-09-20); *Discrete Mathematics* 315–316 (2014), 83–94. https://arxiv.org/abs/1209.4396
- C. Panraksa and A. Tangboonduangjit, *Fixed-point lifting and ghost periodic points for Chebyshev polynomials modulo odd prime powers*, arXiv:2605.04417 (2026). https://arxiv.org/abs/2605.04417
- X. Lu, Y. Dai and C. Li, *Graph Structure of Chebyshev Permutation Polynomials over Binary and Ternary Adic Rings*, arXiv:2605.21819 (2026). https://arxiv.org/abs/2605.21819
