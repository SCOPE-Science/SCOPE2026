# The 64-letter Thue--Morse word has exactly 32 smallest string attractors
## Finding
Let \(t_0=0\) and let \(t_{{n+1}}=t_n\overline{{t_n}}\), where complementation exchanges \(0\) and \(1\). The word \(t_6\) has length \(64\), and the published result \(\gamma(t_6)=4\) says that its smallest string attractors have four positions.

There are exactly \(32\) such smallest attractors. In one-based coordinates they are precisely the sets in the following two families:
\[
\{{16+\varepsilon_1,\;24+\varepsilon_2,\;32+\varepsilon_3,\;48+\varepsilon_4}}\},
\]
and
\[
\{{16+\varepsilon_1,\;32+\varepsilon_2,\;40+\varepsilon_3,\;48+\varepsilon_4}}\},
\]
where every \(\varepsilon_i\in\{{0,1\}}\). Thus each family contains \(16\) attractors. Reflection of the length-\(64\) word exchanges the two families.

The published attractor \(\{{16,24,32,48}}\) is the all-zero member of the first family.

## Assumptions and scope
A string attractor for a finite word \(w\) is a set \(\Gamma\) of positions such that every distinct factor of \(w\) has at least one occurrence whose interval contains a position of \(\Gamma\).

The claim concerns the complete set of smallest attractors of the single canonical Thue--Morse prefix \(t_6\). The value \(\gamma(t_n)=4\) for every \(n\ge4\) is prior work. The index \(n=6\) is the first value for which the source paper's lower bound \(\gamma(t_n)\ge4\) follows directly from its analytic inequality \(\delta(t_n)>3\), rather than from a separate exhaustive check for \(n=4,5\).

## Proof
For each distinct factor \(x\) of \(t_6\), form the position set \(C(x)\subseteq\{{1,\ldots,64}}\) consisting of every position lying in at least one occurrence of \(x\). A position set \(\Gamma\) is a string attractor exactly when
\[
\Gamma\cap C(x)\ne\varnothing
\]
for every distinct factor \(x\). Thus the problem is an exact finite hitting-set problem.

The verifier reconstructs \(t_6\) from the Thue--Morse morphism and computes every factor-cover set in two independent ways. The first groups all substrings by direct interval enumeration. The second first enumerates the distinct factors and then independently finds all overlapping occurrences of each factor. The complete factor-to-cover dictionaries agree.

Removing a cover set that contains another cover set does not change the hitting sets, since hitting the smaller set automatically hits the larger one. There are \(26\) inclusion-minimal cover sets. Exhausting all \(\binom{{64}}{{3}}\) three-position subsets finds none that hits all \(26\), while exhausting all \(\binom{{64}}{{4}}\) four-position subsets finds exactly \(32\).

A second exact-transversal engine recursively branches on an unhit factor-cover set and independently produces the same \(32\) four-position sets. Their one-based forms are exactly the two displayed families. Direct reflection \(p\mapsto65-p\) sends the first family to the second.

## Verification
Run `python3 verify.py` beside `certificate.json`.

The checker regenerates \(t_6\), rebuilds the factor-cover dictionary by two independent occurrence engines, confirms that no three-position attractor exists, enumerates all four-position attractors in two independent ways, and compares the result to the two closed-form families.

The certificate also stores all \(32\) attractors explicitly in one-based coordinates and the exact length-\(64\) Thue--Morse word.

## Relationship to prior work
Kutsukake, Matsumoto, Nakashima, Inenaga, Bannai, and Takeda prove that \(\gamma(t_n)=4\) for every \(n\ge4\), and exhibit the attractor
\[
\Gamma_n=\{{2^{{n-2}},\;3\cdot2^{{n-3}},\;2^{{n-1}},\;3\cdot2^{{n-2}}}}\}.
\]
At \(n=6\) this is \(\{{16,24,32,48}}\). Their theorem establishes the minimum size, not the set of all minimum attractors.

Dolce's later work on factors of the Thue--Morse word again lists \(\Gamma_6=\{{16,24,32,48}}\) as a smallest attractor and develops constructions of a smallest attractor for arbitrary factors, but it does not enumerate all smallest attractors of \(t_6\).

Banbara, Bannai, Guo, Köppl, Mieno, and Okamoto recently made the number and complete characterization of smallest attractors a central question for Fibonacci and period-doubling words. Their 2026 paper completely characterizes those two families and cites the Thue--Morse minimum-size theorem, but does not give an all-attractor classification for Thue--Morse prefixes.

Targeted searches for the exact number \(32\), the length-\(64\) prefix, the published position set, and “all smallest attractors” found the related papers above but no published complete \(t_6\) classification.

## Limitations
This result classifies only \(t_6\). Computation at neighboring dyadic prefixes can suggest further regularity, but no claim about all \(t_n\) is made here.

An unindexed computation by authors working on Thue--Morse attractors could contain the same \(32\)-set census. The inspected published and publicly accessible sources provide particular smallest attractors or minimum sizes, not this complete equality layer.

## References
1. K. Kutsukake, T. Matsumoto, Y. Nakashima, S. Inenaga, H. Bannai, and M. Takeda, “On Repetitiveness Measures of Thue-Morse Words,” arXiv:2005.09524v1, first public version 2020-05-19; SPIRE 2020, DOI 10.1007/978-3-030-59212-7_15.
2. F. Dolce, “String Attractors for Factors of the Thue-Morse Word,” Combinatorics on Words 2023, LNCS 13899, pp. 117–129, DOI 10.1007/978-3-031-33180-0_9.
3. M. Banbara, H. Bannai, P. Guo, D. Köppl, T. Mieno, and Y. Okamoto, “The Smallest String Attractors of Fibonacci and Period-Doubling Words,” CPM 2026, DOI 10.4230/LIPIcs.CPM.2026.33.
