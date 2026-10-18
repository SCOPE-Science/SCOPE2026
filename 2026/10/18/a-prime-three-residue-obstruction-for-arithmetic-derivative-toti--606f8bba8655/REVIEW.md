# Self-review

**Correctness — PASS.** For prime-three exponent \(a\ge2\), normalized derivative \(D(n)/n\ge2/3\) exceeds \(\varphi(n)/n<2/3\) whenever other primes occur; the lone prime-power exception is \(9\). The even-factor obstruction follows from the normalized derivative. Modulo \(3\), equality forces every other prime to be \(2\) modulo \(3\), and then its prime-power factors force an odd number of distinct other primes. Both directions of the exact two-support branch are checked. The standalone checker replays 100000-range examples, not the infinite proof.

**Originality — PASS subject to literature risk.** OEIS A166374 covers known two-prime examples and a construction of general two-prime solutions. The 2011 primary paper treats \(D(n)=an+1\); the closest indexed derivative–cototient support record controls \(D(n)-(n-\varphi(n))\). Exact and alias searches did not uncover the general local prime-three signature or its consequence for *arbitrary-exponent* three-support integers. Absence of a search hit is not a uniqueness certificate. The two-support parameterization is explicitly acknowledged as already covered.

**Value — PASS.** The equation \(D(n)=\varphi(n)\) already has infinite nonsquarefree solution families, making structural exclusion of prime supports meaningful beyond squarefree parity. The result simultaneously forces exponent one for \(3\), all remaining prime residues, and a parity condition on **distinct** remaining prime supports for any solution. It rules out an entire unbounded three-prime-support slice, despite known two-prime families containing \(3\), giving a reusable local sieve rather than a finite check.

Closest sources: OEIS A166374, its 2014 two-prime construction comment, Grau–Oller-Marcén (2011), and a mathematically different indexed derivative–cototient gap result. Later equivalent arguments may exist in unindexed literature.

Self-review: passed. Independent audit: not yet performed.
