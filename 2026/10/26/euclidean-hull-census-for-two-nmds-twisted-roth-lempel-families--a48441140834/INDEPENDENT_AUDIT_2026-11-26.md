# Independent mathematical audit

## correctness

PASS

I reproduced the full census from the defined generator, without using the published symmetric-sum NMDS conditions or executing uploaded code. The generator has rank 5: a nonzero polynomial of degree at most 5 cannot vanish at all 11 evaluation points. A left kernel vector of GG^T yields precisely a hull word by the injective map u↦uG. For NMDS, every four-column subset must be independent, at least one five-column subset must be dependent, and every six-column subset must span F_37^5. Indeed primal distance 8 means the largest nonspanning set has size 5, while dual distance 5 means the smallest dependent set has size 5. Exact residues and rank tests over every four-, five-, and six-subset and all 2592 parameter cases reproduce the totals (hull 0, hull 1)=(1266,30) and (1258,38), the NMDS splits (584,9) and (943,27), both ordered exception lists, and the two NMDS LCD examples. The modular rank routine uses a nonzero pivot and its scaled Schur complement, so it does not rely on numerical rank tolerances.

## originality

PASS

The distance criterion, family, and benchmark examples are known. The three closely relevant GRL sources inspected deal with different evaluation regimes or Hermitian/Galois hulls, and none covers this joint Euclidean hull census. The exact overlap with the benchmark is credited, not claimed as novel; the supported increment is the joint all-parameter classification, including the two example hulls.

## value

PASS

This is a complete parameter selection rule at a benchmark chosen by the originating paper, not a field and sample picked only to obtain a computable example. At identical NMDS distances it locates exactly the non-complementary dual exceptions and shows every such hull is one-dimensional. A researcher using the benchmark who needs a particular Euclidean hull outcome can select parameters from this classification rather than infer it incorrectly from NMDS or rerun a census. This is a finite result, not a claim of general hull control.

The dated certificate retains the supplied scientific assessment, sources and limitations.
