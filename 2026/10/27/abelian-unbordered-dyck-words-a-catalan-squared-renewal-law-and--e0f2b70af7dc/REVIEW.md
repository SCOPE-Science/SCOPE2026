# Scientific review

## Correctness — PASS
For a balanced Dyck path the equality of the prefix/suffix Parikh vectors at a given length is equivalent to zero-height returns at two symmetric positions. This follows from the exact height-to-count identities, without experiment. Splitting at the first paired return gives a unique product decomposition of two Dyck words, and the ordinary Catalan convolution yields the displayed reciprocal series and the shortest-border distribution. The Stirling/telescoping evaluation determines the exact limiting proportion; the singularity proof explicitly addresses the antipodal singularity. `verify.py` independently checks \(290511\) Dyck words and \(19414\) Dyck-word pairs.

## Originality — PASS, with residual risk
The closest primary source is Blanchet-Sadri–Chen–Hawes (2017), whose Theorems 1–3 count abelian borders in unrestricted binary words using an auxiliary Dyck-path representation. Such a count does not determine the distribution after conditioning the input word to lie in the Dyck language, since the source does not refine by original prefix-height nonnegativity. The present Catalan-squared reciprocal and the limiting fraction are different, additional counts. The 2022 survey explicitly discusses abelian borders in unrestricted binary words; the 2021 work on border arrays studies different data. Public sequence/phrase searches and published-record comparisons returned no equivalent Dyck-restricted formula. Another derivation elsewhere, including Catalan enumerations under different terminology, remains possible; this is not a proof of uniqueness.

## Mathematical value — PASS
Abelian borders are a natural relaxed notion of string borders in pattern matching. Dyck words are a canonical nonregular family with Catalan enumeration. Counting their border-free subfamily is a motivated structural question; the shortest-border bivariate distribution and explicit positive limiting density describe all lengths, not arbitrary small examples. The Catalan-squared kernel is the mathematical mechanism that connects symmetric return times to two independent boundary excursions.

## Source and verification limits
Primary text of arXiv:1708.06461 was read in its sections on abelian borders, lattice paths and its count theorems; relevant sections of arXiv:2207.09937 were read. Abstracts and metadata for additional related papers were checked, but full texts of all possibly related sources were not. The newest independent literature search cannot exclude every uncatalogued equivalent. Computations only corroborate the rigorous all-length argument.

Self-review: passed. Independent audit: not yet performed.
