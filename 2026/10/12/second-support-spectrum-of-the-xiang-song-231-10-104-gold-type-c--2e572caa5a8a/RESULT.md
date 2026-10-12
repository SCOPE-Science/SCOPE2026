# Second-support spectrum of the Xiang–Song \([231,10,104]\) Gold-type code

## Finding

For the binary \([231,10,104]\) self-orthogonal code \(C_D\) displayed in Example 2 of Xiang and Song, let \(N_2(s)\) denote the number of two-dimensional subcodes whose union of coordinate supports has size \(s\). The complete spectrum is

\[
N_2=\{{156:440,160:3564,164:13464,168:30558,172:45144,176:43362,180:26664,184:9306,188:1584,192:165\}}.
\]

Hence

\[
d_2(C_D)=156,
\]

and exactly \(440\) two-dimensional subcodes attain the second generalized Hamming weight. Every minimizing two-space has all three nonzero words of Hamming weight \(104\).

## Assumptions and scope

Use the source's field model \(\mathbb F_{2^{{10}}}=\mathbb F_2(\alpha)\), where \(\alpha\) is primitive and satisfies

\[
\alpha^{{10}}+\alpha^6+\alpha^5+\alpha^3+\alpha^2+\alpha+1=0.
\]

Set \(a_1=\alpha\), \(a_2=\alpha^2\), and

\[
D=\left\{{x\in\mathbb F_{{2^{{10}}}}^*:\operatorname{{Tr}}(a_1x^{{33}})=\operatorname{{Tr}}(a_2x^{{33}})=0\right\}}.
\]

The code is

\[
C_D=\left\{{(\operatorname{{Tr}}(bx))_{{x\in D}}:b\in\mathbb F_{{2^{{10}}}}\right\}}.
\]

The claim concerns this explicit source example only. It does not assert a closed formula for all parameters in the Xiang–Song family.

## Proof

The published example gives length \(231\), dimension \(10\), minimum distance \(104\), and weight enumerator

\[
1+132z^{{104}}+396z^{{112}}+396z^{{120}}+99z^{{128}}.
\]

The reconstruction from the displayed primitive polynomial and defining-set equations reproduces exactly these \(231\) coordinates and all \(2^{{10}}-1=1023\) nonzero codewords with the same weight distribution.

Let \(U=\langle u,v\rangle\) be a two-dimensional binary subcode. Its three nonzero words are \(u\), \(v\), and \(u+v\). For every coordinate, the number of these three words that are nonzero there is either zero or two. Therefore

\[
2|\operatorname{{Supp}}(U)|=\operatorname{{wt}}(u)+\operatorname{{wt}}(v)+\operatorname{{wt}}(u+v).
\]

Since every nonzero word has weight at least \(104\), every two-space satisfies

\[
|\operatorname{{Supp}}(U)|\ge156.
\]

The exhaustive census enumerates every two-dimensional message subspace exactly once. A binary two-space has the three nonzero vectors \(\{{u,v,u+v\}}\), so choosing the increasing representative \(u<v<u+v\) gives one representative for each subspace. The number enumerated is

\[
\binom{{10}}{{2}}_2=\frac{{(2^{{10}}-1)(2^9-1)}}{{3}}=174251.
\]

Their direct coordinate-support unions give the stated spectrum. In particular, \(440\) subspaces have support \(156\); one witness is the message two-space with nonzero integer encodings \(3,125,126\), whose three codewords all have weight \(104\). This proves both \(d_2(C_D)=156\) and the exact minimizer count.

## Verification

`artifacts/verify.py` uses only the Python standard library. It implements \(\mathbb F_{{2^{{10}}}}\) from the source polynomial, confirms that \(\alpha\) has order \(1023\), rebuilds \(D\), reconstructs every nonzero codeword, reproduces the published ordinary weight distribution, and then enumerates all \(174251\) two-dimensional subcodes by canonical message triples.

For each two-space it computes the support union directly as a bitset rather than inferring it from a precomputed table. It checks the complete spectrum, \(d_2=156\), the \(440\) minimizers, the Gaussian-binomial total, and an explicit minimizing witness. A successful replay ends with `VERIFY_OK`.

## Relationship to prior work

Xiang and Song construct this Gold-type self-orthogonal family, prove the few-weight distributions, and give the explicit \([231,10,104]\) example with its ordinary weight enumerator. Their article contains no occurrence of “generalized Hamming”, “higher weight”, or “subcode”, and does not state a two-dimensional support census.

The classical generalized-Hamming-weight literature establishes the definition and geometric meaning of \(d_2\), but it does not determine the invariant for this newly displayed code. Exact searches for the parameter string \([231,10,104]\), the Xiang–Song title, the ordinary enumerator coefficients, and the candidate values \(d_2=156\) and \(440\) minimizers located no prior same-object statement. Searches of the published research index likewise returned only different code families and general higher-weight results.

The new information is not implied by the ordinary weight enumerator: the support of a two-space depends on which pairs of codewords sum to each weight class, so pairwise additive incidence data are required in addition to the one-word weight frequencies.

## Limitations

The census is exact for the source's \(m=10\), \(a_1=\alpha\), \(a_2=\alpha^2\) example. It does not classify all binary \([231,10,104]\) codes, and it does not claim a formula for higher-dimensional support spectra of the whole Gold-type family.

The originality comparison is best-of-search. An unindexed older equivalent code could conceivably have the same two-space spectrum without being identified with this construction.

## References

1. Can Xiang and Yishan Song, *Binary self-orthogonal codes with few weights*, Advances in Mathematics of Communications 23 (2026), 146–156, DOI 10.3934/amc.2026017. First public online date: 9 February 2026.
2. V. K. Wei, *Generalized Hamming weights for linear codes*, IEEE Transactions on Information Theory 37 (1991), 1412–1418.
