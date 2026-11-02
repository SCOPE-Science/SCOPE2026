# Scientific review

## Correctness — PASS

The proof gives definitions and quantifiers for a primitive binary word and a proper Abelian border. The reduction of border lengths to at most half the length is exact, including the overlapping case. The centered-height characterization follows by comparing the two circular sums. The finitary proof enumerates every one of the \(2^n\) strings at each integer length \(1\le n\le16\), tests every proper repetition divisor and every root and possible minimal border length, and verifies exactly \(96\) successes forming six orbits only at length \(16\). Both independently written Python and C++ programs were executed with `VERIFY_OK`; the former cross-checks the height formula against substring counting for every primitive input. This is a full finite proof, not an inference from sampling. The only general coprime-content lemma is separately proved, not inferred from samples.

## Originality — PASS, qualified

Charlier et al. (arXiv:1501.07464, §5 Proposition 2) already supply a word of length \(16\) whose conjugates are Abelian bordered through their infinite-word construction. Existence at that length is explicitly **not** new. The inspected section gives neither the impossibility at lengths below \(16\) nor the classification of all six necklaces (and \(96\) labeled words). Holub–Müller (arXiv:1504.02222) concern ordinary unbordered conjugates; that result is neither equivalent to nor stronger than this Abelian classification. Goč et al. (2014) count Abelian-bordered *individual* strings, and Christodoulakis et al. (2014) analyze minimum border lengths per word; their marginal counts do not alone determine the joint rotationwise property. No exact covering classification was identified in the accessible research literature or mathematical-record searches. This is best-knowledge originality, not proof of global priority. The complete text of the 2014 Christodoulakis paper was unavailable, an explicit residual risk.

## Value — PASS

The extremal question is natural: classical primitivity forces ordinary unbordered conjugates, but the Abelian relaxation can eliminate them at every root. Establishing the *first possible length* and all *six* sharp witnesses resolves the exact boundary of this failure, rather than an arbitrary computational slice or merely rediscovering a prior example. The complete necklace classification and balanced-only observation give a compact benchmark for circular border-testing algorithms and for comparing ordinary versus Abelian conjugate phenomena. No higher-order general theorem or applications beyond this motivated sharp cutoff are asserted.

## Remaining risks and limits

The claim is restricted to binary strings through the sharp first length. No count at every larger length, no larger-alphabet statement, and no historical-uniqueness guarantee is implied. The prior 2015 example must retain its attribution. A 2014 article with related title was inspected only through its abstract and bibliographic description; its inaccessible full text leaves residual priority uncertainty, though the abstract concerns single-word border counts, not the rotationwise classification. Independent validation remains to be done.

Self-review: passed. Independent audit: not yet performed.
