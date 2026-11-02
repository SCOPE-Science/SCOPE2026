# Sharp first length and six necklaces for primitive binary words with no Abelian-unbordered conjugate

## Finding

A binary word is *primitive* if it is not a nontrivial integer power of a shorter word. Call it *rotationwise Abelian-bordered* when every one of its cyclic conjugates has an Abelian border: some nonempty proper prefix has the same number of zeros and ones as an equally long suffix.

**Theorem.** Every primitive rotationwise Abelian-bordered binary word has length at least \(16\). At length exactly \(16\), there are precisely \(96\) such labeled words, lying in exactly **six** rotation classes. All are balanced, with eight zeros and eight ones. The lexicographically least representatives of the six classes are:

| Canonical cyclic representative | Number of ones | Shortest Abelian border at this root |
|---|---:|---:|
| `0010101100110011` | 8 | 8 |
| `0010101100110101` | 8 | 8 |
| `0010101101010011` | 8 | 8 |
| `0010110011001101` | 8 | 6 |
| `0010110100110011` | 8 | 8 |
| `0011001100110101` | 8 | 4 |

The six necklaces form three classes if reversal and exchange of zero and one are also allowed. The claim is limited to the sharp first length and its complete list; it does not claim the existence of a length-\(16\) example was previously unknown.

## Assumptions and scope

The alphabet is exactly \(\{0,1}\) and a word \(w=w_0\cdots w_{n-1}\) is a finite string of length \(n\ge 1\). Its rotation rooted at \(s\) is \(w_s\cdots w_{n-1}w_0\cdots w_{s-1}\), with subscripts modulo \(n\). Two factors are Abelian equivalent exactly when their Parikh vectors agree. An Abelian border of a rotation has equal-length, nonempty proper prefix and suffix with equal Parikh vectors. In a binary word it suffices to compare the numbers of ones. The border is permitted to have length greater than half the word, but testing only lengths \(1\le k\le\lfloor n/2\rfloor\) is equivalent to testing all proper lengths, as shown below.

The enumeration takes **every** binary word of lengths \(1,2,\dots,16\), not a heuristic subset, and tests primitivity separately from the border condition. The claim does not assert a census at larger lengths or over larger alphabets.

## Proof

**1. Reduce the border lengths.** A length-\(k\) Abelian prefix-suffix match for a word of length \(n\) is equivalent to a length-\(n-k\) match: subtract the overlapping common middle portion, or equivalently subtract each of the two compared factors from the complete word. Thus if a proper Abelian border exists, one exists with \(1\le k\le\lfloor n/2\rfloor\). For a root \(s\), the direct condition for length \(k\) is
\[
\sum_{j=0}^{k-1}w_{(s+j)\bmod n}
=\sum_{j=1}^{k}w_{(s-j)\bmod n}.
\]

**2. Independent circular-height formulation.** Let \(p\) denote the number of ones in the word, and define a periodic centered height on the circular boundary positions by \(H_0=0\) and
\[
H_{j+1}-H_j=n w_j-p,\qquad H_n=H_0=0.
\]
Then the equality in step 1 is exactly
\[
H_{(s+k)\bmod n}+H_{(s-k)\bmod n}=2H_s.
\]
This identity is used in a second, independently implemented check, rather than being assumed from the direct substring counts.

As a useful general obstruction, if \(0<p<n\) and \(\gcd(n,p)=1\), the \(n\) heights \(H_0,\dots,H_{n-1}\) are distinct: equality of two heights would imply \(n\mid p(j-i)\) for \(0<j-i<n\). A root of the minimum height and a root of the maximum height therefore each have **no** Abelian border, since both neighboring heights at each nonzero circular distance lie strictly on the same side of the root. So no coprime-content word can satisfy the hypothesis. This lemma is not used as a substitute for the exhaustive test of the remaining contents.

**3. Finite exhaustive classification.** The standalone `verify.py` enumerates, for each integer \(n\) with \(1\le n\le16\), all \(2^n\) binary strings exactly once by their zero-padded binary representations. A string is excluded as nonprimitive precisely when there is a proper divisor \(d\mid n\) with \(w_i=w_{i\bmod d}\) for every index. Each primitive string is then tested at every cyclic root \(s\in\{0,\dots,n-1\}\); at each root the program tests all \(1\le k\le\lfloor n/2\rfloor\). It retains the word if every root passes at least one length test. By step 1 this predicate equals rotationwise Abelian-borderedness, and by the divisor test the retained words are exactly the primitive ones.

The enumerator finds no retained word for lengths \(1\) through \(15\). At length \(16\) it finds exactly \(96\), all of content \((8,8)\). Replacing each retained word by its lexicographically minimal conjugate produces precisely the six displayed representatives. Every displayed representative has \(16\) distinct roots, so \(6\cdot16=96\). A separate C++ enumeration (`independent_check.cpp`) constructs the binary strings and running circular prefix/suffix counts independently and reproduces these counts and representatives. The Python code independently tests the circular-height identity on every primitive word encountered, finding perfect agreement with direct counting.

**4. Explicit witnesses.** In the next table the sixteen integers correspond in order to cyclic starting positions \(s=0,1,\dots,15\). Each entry is the *shortest* Abelian border length of that rotation, so the table supplies an explicit witness for every root of every representative. Every integer is between \(1\) and \(8\).

| Canonical representative | Shortest border lengths for its 16 roots |
|---|---|
| `0010101100110011` | `8,1,4,2,2,2,4,1,8,1,4,1,4,1,4,1` |
| `0010101100110101` | `8,1,8,2,2,2,4,1,8,1,8,1,4,2,2,2` |
| `0010101101010011` | `8,1,4,2,2,2,8,1,8,2,2,2,4,1,8,1` |
| `0010110011001101` | `6,1,6,2,8,1,8,1,4,1,4,1,8,1,8,2` |
| `0010110100110011` | `8,1,8,2,6,1,6,2,8,1,8,1,4,1,4,1` |
| `0011001100110101` | `4,1,8,1,4,1,4,1,4,1,8,1,4,2,2,2` |

The enumeration of all binary strings up through length \(16\), combined with the exact predicate in steps 1–2 and the witness list above, proves both the lower bound and the complete equality classification. Nothing about lengths greater than \(16\) is inferred from this finite calculation.

## Verification

Run with Python 3 and a standard C++17 compiler, respectively:

```sh
python3 verify.py
c++ -std=c++17 -O2 independent_check.cpp -o independent_check
./independent_check
```

Each program terminates with `VERIFY_OK`; the Python program also prints the class representatives and all shortest-border witness vectors. Both programs were executed successfully. The two enumerators use different primitivity implementations and enumeration order; the Python implementation additionally compares direct Abelian-border counts with the independent centered-height identity at every primitive word. The code is complete and uses no external datasets, dependencies, or unprovided computations.

## Relationship to prior work

Charlier, Harju, Puzynina and Zamboni [1], Proposition 2, established an infinite-word construction with all sufficiently long factors Abelian bordered. Their explicit block `0101001100110011` already yields a length-\(16\) example when its rotations appear as factors of an allowed infinite concatenation. Its canonical rotation is `0011001100110101`, one of the six listed here. **The existence of a length-\(16\) example is therefore prior work, not claimed here as novel.** That proposition does not establish that smaller primitive words are impossible or classify the six shortest necklaces.

Holub and Müller [2] study **ordinary** bordered/unbordered conjugates: a primitive binary word always has at least two ordinary unbordered conjugates. Their term *fully bordered* has a different meaning from the Abelian property here and does not preclude all conjugates being Abelian bordered. Goč, Rampersad, Rigo and Salimov [3] count individual Abelian-bordered binary strings; those one-word marginal counts do not determine whether *all* conjugates of a single primitive word are Abelian bordered. Christodoulakis and collaborators [4] similarly analyze shortest Abelian borders and counts of individual binary words. The inspected accessible material does not give this sharp six-necklace rotationwise classification; the full text of [4] was not accessible, leaving a literature-priority caveat.

## Limitations

This is a finite, exhaustively reproducible cutoff and classification at length \(16\), not a formula for counts at arbitrary lengths. The general coprime-content observation is elementary; mathematical value resides in the exact first failure and complete classification under rotation. The proof relies on transparent, finite exhaustive computation, for which the full code and cross-checks are provided. Earlier unindexed classifications cannot be ruled out, and independent mathematical audit has not been performed.

## References

[1] É. Charlier, T. Harju, S. Puzynina, L. Q. Zamboni, *Abelian bordered factors and periodicity*, arXiv:1501.07464 (first public 2015-01-29), §5 Proposition 2. https://arxiv.org/abs/1501.07464

[2] Š. Holub and M. Müller, *Fully bordered words*, arXiv:1504.02222 (first public 2015-04-09), introduction and §1. https://arxiv.org/abs/1504.02222

[3] D. Goč, N. Rampersad, M. Rigo, P. Salimov, *On the Number of Abelian Bordered Words (with an Example of Automatic Theorem-Proving)*, International Journal of Foundations of Computer Science 25(8), 1097–1110 (2014). https://doi.org/10.1142/S0129054114400267

[4] M. Christodoulakis, M. Christou, M. Crochemore, C. S. Iliopoulos, *Abelian borders in binary words*, Discrete Applied Mathematics 171, 141–146 (2014). https://doi.org/10.1016/j.dam.2014.02.012
