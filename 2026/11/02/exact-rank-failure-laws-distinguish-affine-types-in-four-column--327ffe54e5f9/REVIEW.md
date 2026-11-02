# Scientific review

## Correctness — PASS
The claimed domain is all \(d\ge3\), exactly four distinct Walsh-coordinate columns, and either iid uniform sampling or uniform sampling without replacement. Scaling and nonzero column signs cannot change rank. The three binary differences after translating one column have rank exactly two or three; this proves the two projective designs. Every affine plane in the real cube contains at most four vertices, and exactly twelve four-vertex sets lie in one; the proof checks the six coordinate faces and six diagonal planes and excludes others. Exact occupancy inclusion--exclusion yields both stated probability laws. Their deterministic row-count horizons, asymptotics and strict with-replacement ordering follow algebraically. All essential finite identities were replayed by the embedded verifier. There are no extrapolated infinite deductions from the finite checks.

## Originality — PASS, qualified
The motivating 2022 Balabanov--Beaupère--Grigori--Lederer full-text sections 1--3 and embedding theorem and the supporting Tropp 2010/2011, Boutsidis--Gittens 2012/2013 and Holodnak--Ipsen 2013/2014 works treat SRHT/OSE bounds, general row sampling and rank criteria. Their statements do not imply either of the displayed exact four-coordinate probability formulas without the new explicit Walsh affine-type and cube coplanarity analysis. The 2019 Jung--Kueng--Mixon design discussion supplies related Walsh sign independence but not this sampling rank law. Published research-record comparisons retrieved Walsh four-support *Fourier uncertainty*, spectral bases and DFT minors, different target quantities, not a covered row-sampled least-squares rank-failure classification. Source-index incompleteness and possible specialized results on cube random-matrix rank remain publication-priority risks; this review makes no independent novelty certification.

## Value — PASS
Rank failure is a definitive breakdown of injectivity for structured-sketch least squares and subspace embeddings. All four-column coordinate subspaces have exactly the same row leverage scores \(4/N\), yet their rank-failure exponents and sharp no-replacement guarantees differ. The exact classification exposes a concrete limitation of coherence-only descriptions and supplies finite-size benchmarks for sampling algorithms. The exact threshold gap is of order \(N\), not a tiny numerical improvement. No broader algorithmic convergence or conditioning result is claimed.

## Scope and remaining risks
Only four coordinate columns and the standard Walsh--Hadamard sampling design are covered; the proof is exact arithmetic. The designated source has first-public date 2022-10-20. Classical combinatorial identities are acknowledged. Independent publication-priority and proof audit have not been completed.

Self-review: passed. Independent audit: not yet performed.
