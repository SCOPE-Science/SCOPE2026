# Exactly \(32{,}530\) binary rank-two theories with successor

## Finding

There are exactly **\(32{,}530\)** complete first-order sentence theories of quantifier rank at most two realized by finite binary words in which **both** symbols occur, in the language containing the linear order, immediate-successor relation, and the two letter predicates. Every such theory has a representative of length at most **\(24\)**. The bound is attained: precisely **\(16\)** theories have shortest representative length \(24\).

Counting the empty word as well, the full binary-word quotient has \(32{,}541\) rank-two classes. Of these, one is the empty-word class and ten are classes of nonempty monochromatic words (five for each colour), leaving \(32{,}530\) mixed-word classes.

## Assumptions and scope

A finite binary word \(w=w_1\cdots w_n\), with \(n\geq0\), is viewed as a relational structure whose domain is \(\{1,\ldots,n\}\), equipped with strict order \(<\), the immediate-successor relation \(S(i,j)\) holding exactly when \(j=i+1\), and unary predicates \(P_0,P_1\) identifying the respective letters. There are **no named endpoint constants**, and successor is a primitive predicate rather than an abbreviation that costs an additional quantifier. Formulas use ordinary first-order quantifiers, no counting quantifiers, and unrestricted finite formulas. Their quantifier rank is maximum nesting depth. Two words agree at rank two when they satisfy exactly the same closed formulas of rank at most two. This is also the depth-two fragment of two-variable first-order logic on these word structures.

For a position \(i\), write its *local witness profile* as
\[
\pi_w(i)=(c,L_f,L_1,R_1,R_f),
\]
where \(c=w_i\); the sets \(L_f=\{w_j:j\le i-2\}\) and \(R_f=\{w_j:j\ge i+2\}\) record colours occurring strictly beyond an immediate neighbour; and \(L_1=\{w_{i-1}\}\) or the empty set according as a predecessor exists, with \(R_1\) defined similarly. Thus each of the last four entries is a subset of \(\{0,1\}\), while \(L_1,R_1\) are empty or singletons. Define
\[
T(w)=\{\pi_w(i):1\le i\le n\}.
\]
In particular \(T(\epsilon)=\varnothing\).

## Proof

**Lemma 1 (logical completeness of the profiles).** For finite binary words \(u,v\), their rank-two sentence theories agree if and only if \(T(u)=T(v)\).

*Proof.* With one named element \(x\), quantifier-free assertions in two variables \(x,y\) distinguish precisely the colour of \(x\), the colour of \(y\), and the five mutually exclusive positions of \(y\) relative to \(x\): equal, immediately left, farther left, immediately right, or farther right. At quantifier rank one with \(x\) free, a formula is a Boolean combination of atomic information about \(x\) and assertions of the form \(\exists y\,\alpha(x,y)\), where \(\alpha\) is quantifier-free. Thus its truth depends exactly on \(\pi_w(x)\). Conversely, the exact local profile is expressible by a finite conjunction specifying, for each colour and each relative position class, whether a suitable \(y\) exists. The rank is at most one. A rank-two sentence is a Boolean combination of statements about existence of positions with specified rank-one pointed types: it can be converted to Boolean combinations of \(\exists x\,\theta(x)\) with \(\theta\) of rank at most one. Any closed rank-one subformula embedded in \(\theta\) is determined by the same presence profile data. Consequently agreement of realized profiles implies agreement of all rank-two sentences, and the sentence \(\exists x\,\theta_{\pi}(x)\) detects the presence of each individual profile. \(\square\)

**Lemma 2 (exact right-append transfer).** There is a deterministic operation \(F_a\) on realizable profile sets such that \(T(wa)=F_a(T(w))\), for each \(a\in\{0,1\}\).

*Proof.* If \(w\) is empty, the new profile is \((a,\varnothing,\varnothing,\varnothing,\varnothing)\). Otherwise exactly one realized profile has empty right-neighbour set: it is the profile \(p=(c,L_f,L_1,\varnothing,\varnothing)\) of the last position. Every old **nonlast** profile \((c',A,B,C,D)\) transforms to \((c',A,B,C,D\cup\{a\})\), because the appended position is at distance at least two to the right. The old last profile transforms to \((c,L_f,L_1,\{a\},\varnothing)\). The fresh last position contributes
\[
(a,L_f\cup L_1,\{c\},\varnothing,\varnothing).
\]
Taking the set of these transformed profiles therefore depends only on \(T(w)\), and equals \(T(wa)\). \(\square\)

**Lemma 3 (exhaustive finite census).** The least subset of abstract profile states containing \(\varnothing\) and closed under the two transfers \(F_0,F_1\) contains exactly \(32{,}541\) states. The greatest breadth-first discovery depth is \(24\), and exactly \(16\) states are first discovered there.

*Proof.* Each profile is packed into ten bits: two bits each for the one-hot colour, far-left set, adjacent-left set, adjacent-right set, and far-right set. A state is the bitset of the profiles realized; the empty state is zero. `verify_transfer.py` implements precisely the two cases of Lemma 2 as integer bit operations, starting at state zero and applying both transfers to every discovered state. Its entire breadth-first search terminates after checking exactly \(65{,}082\) directed transitions out of \(32{,}541\) states. The resulting count-by-first-discovery-depth vector (depth \(0\) through \(24\)) is
\[
(1,2,4,8,16,32,62,118,222,414,742,1256,1968,2824,3688,4312,4504,4168,3360,2352,1408,696,280,88,16).
\]
Because every word is obtained from the empty word by a succession of append operations, Lemma 2 proves **global completeness**, not merely completeness through a chosen word length. By breadth-first order, first-discovery depth is precisely the minimum possible representative length for that state. The program additionally recomputes every encountered transition from an explicit representative word as a cross-check. `verify_direct.py` independently enumerates the same reachable signatures using literal colour/relative-position witness pairs rather than packed-transfer operations and reproduces the complete count and depth distribution. The exact outputs, all sixteen length-\(24\) minimal witnesses, and a canonical digest of the complete state set are in `CERTIFICATE.json`. \(\square\)

**Conclusion.** For each fixed colour there are five monochromatic states, represented by words of lengths \(1,2,3,4,5\), with all greater lengths sharing the fifth theory. (This also follows directly by comparing their local profiles.) Removing these ten states and the empty state from Lemma 3 leaves \(32{,}530\) states represented by words containing both colours. All sixteen states at depth \(24\) have representatives containing both colours, proving the asserted sharp bound. Lemma 1 translates these combinatorial states back into distinct rank-two first-order theories. \(\square\)

## Verification

Run `python3 verify_transfer.py` and `python3 verify_direct.py` from the directory containing these files. The first program emits the canonical JSON in `CERTIFICATE.json`; the second prints an independently computed tuple of the total count, mixed-colour count, sharp depth, and distribution. The expected complete state count is \(32{,}541\), mixed count \(32{,}530\), sharp depth \(24\), and the canonical state-set SHA-256 is `a0a1f4f7049b3dd18ba1297669ceac92d0d04ddb4bd59f50ee33a23deb82b16b`. The code uses only Python's standard library. Every packed state is serialized as a \(128\)-byte big-endian nonnegative integer and those byte strings are lexicographically sorted before hashing.

The finite enumeration constitutes the computational portion of the proof; the two lemmas establish that its search space exhausts all finite words. The recorded stdout in `direct_verification.txt` gives the independent computation's complete depth distribution. The digest checks reproduction of the counted set but is not, by itself, evidence of mathematical correctness.

## Relationship to prior work

Weis and Immerman (2009), especially their Theorem 5.4 and successor-ranker framework in Section 5, characterize depth-bounded two-variable logic on words with successor at **all** depths and alphabets. The present rank-two pointed-profile lemma is a deliberately simpler specialization; its general logical expressibility content is not presented as a new characterization. The additional quantitative content is the exact \(32{,}530\)-class mixed-binary index of this fragment and the sharp \(24\)-position minimal-representative bound, obtained from the explicit finite transition census. These numbers were not found stated in the inspected primary text. Kallas, Kufleitner and Lauser (2010) give algebraic and topological characterizations of related two-variable successor fragments, not an exact depth-two binary quotient census in the material inspected.

## Limitations

The theorem depends on the vocabulary **exactly** specified above: in particular, adding endpoint constants, dropping the successor predicate, or adding counting quantifiers changes the invariant. No estimate at greater quantifier rank or for larger alphabets is claimed. Numerical completeness relies on running the supplied finite-state computation together with the proved transfer lemma; a finite run without that lemma would not establish the infinite-word statement. The novelty comparison does not rule out an earlier specialized enumeration or a numerical corollary in uninspected literature, and no independent mathematical audit has been performed.

## References

1. P. Weis and N. Immerman, *Structure Theorem and Strict Alternation Hierarchy for FO² on Words*, Logical Methods in Computer Science 5(3), 2009, arXiv:0907.0616, https://arxiv.org/abs/0907.0616. Earlier public version: ECCC TR07-008, https://eccc.weizmann.ac.il/report/2007/008/.
2. J. Kallas, M. Kufleitner and A. Lauser, *First-order Fragments with Successor over Infinite Words*, arXiv:1101.0115 (2010), https://arxiv.org/abs/1101.0115.
