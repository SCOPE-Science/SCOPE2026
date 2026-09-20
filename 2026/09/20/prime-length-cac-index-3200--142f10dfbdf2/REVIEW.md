# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The reduction to a finite gap is exactly the one used in Hsia--Li--Sun (2023). Their Theorem 5.2 covers all subgroup indices \(\ell\le3000\). For \(3001\le\ell\le3200\), their Theorem 5.1 covers every index with \(\omega(\ell)\le3\), leaving exactly twenty indices with four distinct prime factors. For each remaining index, the earlier reported computation covers \(p\le2^{30}\) and their analytic theorem covers \(p\ge B(\ell)\), so only the explicitly enumerated interval \(2^{30}<p<B(\ell)\) remains.

The verification artifact exhaustively enumerates this interval subject to the defining subgroup-index condition and obtains exactly 165 primes. For each prime, it deterministically constructs a primitive root \(g\) and elements \(b,c\) with \(b\in gH\), \(c\in g^2H\), and \(1+b+c=0\). These conditions are checked by exact modular arithmetic. They imply the generator-coset conjecture and hence the twisted-Fermat formulation used by the cited construction.

The CAC-size formula then follows from the published Fu--Lo--Shum upper bound and construction mechanism when \(4\nmid\operatorname{ord}_p(2)\); the \(4\mid\operatorname{ord}_p(2)\) branch is the classical equi-difference case.

## Originality

**PASS, to the best of our knowledge.** The directly matching 2023 paper states a universal consecutive subgroup-index theorem only through \(\ell\le3000\), after combining its analytic bound with finite computations. Its Theorem 5.1 separately covers larger indices with one, two, or three distinct prime factors. The 2024 cyclotomic-number paper proves the conjecture when \(\ell\) is an odd prime and explicitly identifies composite \(\ell\) as the obstacle for that method. The twenty new indices here are composite and have four distinct prime factors, so that theorem does not subsume them.

Searches for the exact conjecture, the values 3000/3200, the first uncovered index 3003, and later work citing the 2023/2024 papers did not locate a source extending the full consecutive range past 3000. No overlapping SCOPE record was located under conflict-avoiding-code, cyclotomic-number, or synonymous searches.

The main residual risk is Ma--Zhao--Shen (2014), whose full text was not directly inspected. Its accessible abstract is broad, while the later Hsia--Li--Sun papers explicitly describe the relevant generator-coset statement as conjectural and attribute only the \(p\le2^{30}\) computational verification to Ma--Zhao--Shen. An equivalent finite extension could also exist in an unindexed computational note or under protocol-sequence terminology.

## Value

**PASS.** The result moves the strongest located uniform subgroup-index guarantee from 3000 to 3200 and resolves every first obstruction created by four-prime-factor composite indices in this interval. It does so with an auditable finite certificate: exhaustive code regenerates and verifies all 165 primitive-root coset witnesses, confirms there are no omitted gap primes, and emits a canonical witness digest. The corollary gives the exact optimum size of every prime-length, weight-three CAC in this enlarged consecutive index range.

## Scientific limitations

This is a finite-range extension rather than a new asymptotic method or a proof for arbitrary composite subgroup index. The argument depends on two published ingredients: the reported small-prime verification and the Hsia--Li--Sun large-\(p\) bound. The computational artifact is exact but limited to the stated index interval. Originality remains to the best of our knowledge, with the source-access and terminology risks described above.
