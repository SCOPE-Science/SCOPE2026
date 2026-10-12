# Exact binary length-fourteen substring-composition ambiguity census

## Finding

For a binary word of length \(14\), observe the **multiset**, with multiplicities, of the Parikh vectors of every nonempty contiguous substring. Two words are *equicomposable* if their observations coincide. The exact maximum observation-fiber size is

\[E_{14}=4.\]

The complete size distribution of observation fibers is: \(128\) singleton fibers, \(8104\) fibers of size \(2\), and \(12\) fibers of size \(4\). Thus exactly \(8244\) distinct observations arise from the \(16384\) words. All \(128\) singleton words are palindromes, all size-two fibers are reversal pairs, and the twelve size-four fibers consist of two reversal pairs each. The standalone `ambiguous_classes.json` lists every size-four fiber exactly, and includes a representative such as `00010000110001`, together with its three equicomposable partners `00011000100001`, `10000100011000`, and `10001100001000`.

Equivalently, precisely \(48\) of the \(16384\) words are not reconstructable up to reversal. For a uniformly sampled fourteen-bit word the non-reconstructability probability is \(3/1024\).

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\). A word has exactly \(14\) symbols. Its observations include the composition of **every** contiguous substring of each length from \(1\) through \(14\), including repeated compositions with their exact occurrence multiplicities. Composition means the ordered pair (number of zeros, number of ones), **not** the ordered substring. The observer does not learn substring positions. The claim concerns labeled binary strings, including each reversal as a separate word when distinct; it is neither a statement about substring sets without multiplicity nor one about other lengths or alphabets.

For \(w=(b_0,\ldots,b_{13})\), define prefix sums \(p_0=0\) and \(p_j=\sum_{i=0}^{j-1}b_i\) for \(1\le j\le14\). For lengths \(1\le\ell\le14\) and counts \(0\le r\le\ell\), define

\[c_{\ell,r}(w)=\#\{i:0\le i\le14-\ell,\ p_{i+\ell}-p_i=r\}.\]

The array of these counts is the complete observation: length and number of ones uniquely determine the binary Parikh vector.

## Proof

1. Every nonempty contiguous substring of \(w\) is represented uniquely by a pair of positions \((i,i+\ell)\), with \(1\le\ell\le14\) and \(0\le i\le14-\ell\). Its number of ones is exactly \(p_{i+\ell}-p_i\). Therefore two words are equicomposable if and only if **all** their corresponding integer counts \(c_{\ell,r}\) are equal. This equivalence is exhaustive: no substrings or multiplicities are omitted.

2. The program `verify_direct.py` visits each of the \(2^{14}=16384\) binary words **exactly once**, generating all tuples of length \(14\) over \(\{0,1\}\). For every word it independently sums symbols in each positional window of each permissible length, and stores the full count vector in a dictionary keyed by exact integer tuples. Consequently the dictionary values are precisely the equivalence classes of the observation relation, with neither rounding nor hash collisions affecting equality (tuple-key equality checks every component).

3. Exhausting that finite domain gives \(128\) classes of size \(1\), \(8104\) of size \(2\), and \(12\) of size \(4\), with no other classes; the sum \(128+2\cdot8104+4\cdot12=16384\) is a coverage check. All twelve size-four classes are recorded as complete sorted lists in `ambiguous_classes.json`. The largest class therefore has exactly four members: its existence is exhibited by the listed quadruples, and no class can be larger because the exhaustive partition has no other sizes.

4. An independently written C++ verifier, `verify_correlations.cpp`, represents a word by its \(15\) prefix sums and counts **all positive-length prefix-sum differences** over pairs of endpoints. It groups words by these exact integer arrays using ordered maps, rather than the Python substring summation and dictionary. It reaches the same histogram and exactly the same twelve four-word fibers. This provides a separate reconstruction of the finite calculation. Reversal invariance gives a distinct partner for every nonpalindrome, while a length-fourteen binary palindrome is determined by its first seven bits. Hence all \(128\) singleton fibers are precisely the palindromes, and all size-two fibers are reversal pairs.

The argument is a **complete, finite exhaustive proof** for length fourteen. It does not extrapolate from a sampled range or assert a theorem for larger lengths.

## Verification

With Python 3, run `python3 verify_direct.py`; it prints one JSON object containing the word count, exact full fiber histogram, and the twelve sorted four-word fibers. With a C++17 compiler, run `c++ -std=c++17 -O2 verify_correlations.cpp -o verify_correlations` followed by `./verify_correlations`; it prints the same summary and four-word fibers. Compare the two independently produced class lists against `ambiguous_classes.json`. Both executables were run on the supplied source and their lists matched. The Python program explicitly asserts the claimed histogram; the C++ program checks it using assertions. No external libraries, data or inaccessible auxiliary results are required for reproduction.

## Relationship to prior work

Acharya, Das, Milenkovic, Orlitsky, and Pan defined equicomposability and gave a polynomial characterization and interleaving constructions. Their 2014 full preprint establishes \(4\le E_{14}\le8\) from the general prime-factor-based bounds: here \(14+1=3\cdot5\), for which their upper bound yields \(2^{4-1}=8\), while their lower construction gives \(2^{1+1}=4\). Their exact equality theorems cover lengths one below prime powers or twice prime powers, **not** fourteen. This work supplies the missing finite upper bound and the full equality census at the smallest case where the length plus one has two distinct odd prime factors. The general polynomial characterization alone does not state or evaluate these class multiplicities.

The same authors' 2010 conference paper is a predecessor covering general reconstruction, constructions and bounds. Its accessible abstract was compared, not its complete paper. Later work on algebraic reconstruction algorithms addresses efficient reconstruction and coding; the inspected abstract does not state this precise maximum or equality census. Published related records and focused searches did not identify a prior exact table at these parameters; that absence is **not** a proof of global novelty.

## Limitations

This is an exact finite result, not an infinite-family classification or a new algorithmic time bound. The complete proof is computer-assisted and depends on the ability to inspect and execute the two short standalone programs. The 2010 conference paper and a relevant later algorithm paper were not inspected in full, so an earlier unindexed explicit census remains a bibliographic risk. The archived public version dated March 10, 2014 supplies the earliest **day-verified** full-text source used here; the earlier 2010 conference publication is known only to year precision from the inspected record and is not silently assigned a date.

## References

1. J. Acharya, H. Das, O. Milenkovic, A. Orlitsky, and S. Pan, *String Reconstruction from Substring Compositions*, arXiv:1403.2439v1, first posted March 10, 2014, https://arxiv.org/html/1403.2439v1. Especially Sections 2, 8, 10, 11, and the conclusions.
2. J. Acharya, H. Das, O. Milenkovic, A. Orlitsky, and S. Pan, *On Reconstructing a String from Its Substring Compositions*, IEEE International Symposium on Information Theory (2010), pp. 1238–1242, doi:10.1109/ISIT.2010.5513668.
3. U. Gupta and H. Mahdavifar, *A New Algebraic Approach for String Reconstruction from Substring Compositions*, arXiv:2201.09955 (2022); related method, abstract inspected, https://arxiv.org/abs/2201.09955.
