# Complete classification of shortest ternary crucial Abelian-cube-free words

## Finding

There are **exactly 264 labeled shortest crucial Abelian-cube-free words** over the alphabet \(\{0,1,2\}\). They form **44 classes under global permutation of the three letters**, with six words in every class. Every shortest crucial word has length \(11\), and its three one-letter right extensions are forced to end in Abelian cubes whose constituent block lengths are exactly \(1\), \(2\), and \(4\), in some order.

Here is an explicit, nonredundant list of representatives. Let \(\mathcal A\) be the twelve permutations of the multiset \(\{0,0,1,2\}\), and let
\[
\mathcal B=\{0201,0210,2001,2010\}.
\]
Choose \(A\in\mathcal A\) and \(B\in\mathcal B\), except for the four pairs
\[
(A,B)\in\{1200,2100\}\times\{0201,0210\}.
\]
The **44** words \(AB100\) are exactly one representative per alphabet-permutation class. Permuting their alphabet labels in all six possible ways gives all **264** words. The attached `canonical_representatives.csv` lists the 44 representatives explicitly.

## Assumptions and scope

A factor of a finite word is an *Abelian cube* if it is the concatenation of three nonempty consecutive blocks of equal length with identical Parikh vectors (counts of each alphabet symbol). A word is *Abelian-cube-free* when none of its factors is an Abelian cube. It is *crucial* when it is Abelian-cube-free but appending **any** of the three letters on the right creates an Abelian cube. Alphabet letters are labeled, so distinct words are counted separately; *relabeling equivalence* identifies words differing by one global permutation of the three labels. A block length \(r\) refers to the length of **each** of the three blocks, not the full cube length.

All claims concern words over the full prescribed ternary alphabet. Minimal length \(11\) is a previously established theorem of Glen, Halldórsson, and Kitaev (first publicly available in 2008); the new claim is the complete list, the exact enumeration, and the forced witness-length profile.

## Proof

**1. Right-extension witnesses.** Let \(w\) be any length-\(11\) crucial word. An Abelian cube occurring after appending one letter must end at that appended letter, because \(w\) contains no such factor. If the three equal blocks each have length \(r\), then \(3r\le12\), so \(r\in\{1,2,3,4\}\). For fixed \(r\), at most one appended letter works: the Parikh vector of the first two blocks determines the required Parikh vector of the final block, and hence fixes its missing last letter. Since three *different* appended letters must each create a cube, three different witness lengths are required.

**2. The witness length \(3\) is impossible.** Number the positions of \(w\) from \(0\) through \(10\). There are three possibilities for a three-element subset of \(\{1,2,3,4\}\) containing \(3\).

If the witness lengths are \(\{1,2,3\}\), call the letters appended for lengths \(1,2,3\) respectively \(u,v,t\). All are distinct. The length-\(1\) cube forces \(w_9=w_{10}=u\). The length-\(2\) cube forces \(w_8=v\) and \(\{w_6,w_7\}=\{u,v\}\) as multisets, so positions \(6,7,8\) contain one \(u\) and two \(v\)'s. But the length-\(3\) cube forces positions \(6,7,8\) to have the same multiset as \(w_9w_{10}t=uut\). Contradiction.

If the witness lengths are \(\{1,3,4\}\), call their appended letters \(u,v,t\), respectively. The length-\(1\) witness again gives \(w_9=w_{10}=u\). The length-\(3\) witness makes each of the blocks at positions \(3\ldots5\) and \(6\ldots8\) contain exactly two \(u\)'s and one \(v\). In particular, positions \(4\ldots7\) contain no \(t\), while \(w_8\ne t\). But the length-\(4\) witness requires its three four-letter blocks to have identical compositions; the last block, \(w_8uut\), has exactly one \(t\), whereas its middle block, \(w_4\ldots w_7\), has none. Contradiction.

If the witness lengths are \(\{2,3,4\}\), call the corresponding appended letters \(z,y,x\), respectively, all distinct. The length-\(4\) witness implies that the counts in \(w\), reduced modulo three, are \(2x\) (two occurrences of \(x\), modulo three). The length-\(3\) witness implies that the counts in the suffix \(w_3\ldots w_{10}\), reduced modulo three, are \(2y\). Consequently the first three positions have exactly the multiset \(2x+y\). Similarly the length-\(2\) witness shows the first six positions have counts congruent to \(2x+z\) modulo three. Because they already contain \(2x+y\) in their first three positions and have total length six, their only possible multiset is \(2x+3y+z\). Hence positions \(3\ldots5\), and by the length-\(3\) witness also positions \(6\ldots8\), have multiset \(2y+z\). The final two positions have multiset \(y+z\). If \(w_{10}=z\), the length-\(2\) witness requires all of positions \(6\ldots9\) to be \(z\), contradicting \(2y+z\) at positions \(6\ldots8\). If \(w_{10}=y\), then \(w_9=z\), and equality of the last two length-\(2\) blocks forces \(w_8=y\). The last four positions after appending \(x\) then contain exactly one \(x\), whereas the first four contain at least two \(x\)'s. This contradicts the length-\(4\) witness. Thus length \(3\) cannot occur in any triple of witness lengths.

It follows that the witness lengths are exactly \(\{1,2,4\}\), and each appended letter has exactly its assigned length, since no further possible length remains.

**3. Forced normal form.** Relabel the alphabet so that appending \(0\), \(1\), and \(2\) yields witness lengths \(1\), \(2\), and \(4\), respectively. The length-\(1\) witness gives the final two letters \(00\). The length-\(2\) witness divides the final six letters after appending \(1\) into three pairs, each of multiset \(\{0,1\}\). The final pair is \(01\), so the two preceding pairs are \(01\) or \(10\), and the five-letter suffix of \(w\) must be \(01100\) or \(10100\). In particular the final three letters are \(100\), and the four positions immediately before them end in \(01\) or \(10\).

The length-\(4\) witness partitions \(w2\) into three four-letter blocks of identical composition. The last block is \(1002\), containing precisely two zeros, one one, and one two. Therefore \(w=AB100\), where both \(A\) and \(B\) are permutations of \(0012\), and \(B\) ends in \(01\) or \(10\). The only possibilities for \(B\) are exactly the four members of \(\mathcal B\) stated above.

**4. Checking cube avoidance without extrapolation.** Every one of the \(12\cdot4=48\) candidate words contains exactly two copies of the letter \(2\). An Abelian cube's count of each symbol is divisible by three; therefore no cube in a candidate can contain \(2\). Every length-nine factor contains the \(2\) in the middle block \(B\), so length-nine cubes are impossible. A length-six factor free of \(2\) is possible only if \(B\) begins with \(2\), in which case the only such factor is the last six letters: either \(001100\) or \(010100\). Neither is a length-six Abelian cube. Each of \(A\), \(B\), and the terminal \(100\) contains no run of three equal symbols. The only length-three Abelian cube that could cross a block boundary is \(000\), occurring exactly when \(A\) ends in \(00\) and \(B\) begins in \(0\). This happens precisely for \(A\in\{1200,2100\}\), \(B\in\{0201,0210\}\), giving exactly four forbidden pairs. Thus precisely \(48-4=44\) normal-form candidates are Abelian-cube-free.

Conversely, each of these 44 candidates has the promised suffix cubes after appending each of \(0,1,2\), by their one-, two-, and four-block composition constraints. Hence each is crucial. A crucial word has a *unique* appended-letter-to-witness-length assignment by step 2, so exactly one permutation of its alphabet labels puts it into the described normal form. All three labels occur in every candidate, giving six distinct labelings per normal-form word and \(44\cdot6=264\) words overall.

## Verification

The included `verify.py` uses only the Python standard library. Run `python3 verify.py` beside the other files. It independently enumerates all \(3^{11}=177147\) labeled ternary words, tests every possible factor for Abelian cubes, and checks each of the three one-letter extensions. The program compares this direct classification to the structurally generated family, checks that none of the \(3^n\) words with \(n<11\) is crucial, verifies 44 relabeling orbits, and reports the six witness-length permutations. It also confirms the independently published count of \(50520\) ternary Abelian-cube-free words of length \(11\).

The complete analytic proof above establishes the infinite quantifiers relevant to the structural characterization; the finite checker is an independent exhaustive consistency check for the single finite length under study, not an extrapolation to arbitrary lengths.

## Relationship to prior work

Glen, Halldórsson, and Kitaev proved that the minimum possible length of a ternary crucial Abelian-cube-free word is \(11\), and gave examples and constructions for varying alphabet sizes. That length theorem is used here, not claimed as new. Their 2008 preprint and 2010 article were compared at the level of the stated extremal results and their ternary examples: they do not state the above complete 44-family characterization or the count 264. Aberkane, Currie, and Rampersad previously tabulated \(50520\) *all* ternary Abelian-cube-free words of length 11; this count neither identifies which of those are crucial nor implies their 44-orbit classification.

## Limitations

This is a classification at the established shortest ternary length only. It does not count longer crucial words or classify larger alphabets. The literature comparison supports originality against the identified principal primary references, but cannot rule out every independently obtained or unindexed equivalent enumeration. The proof and finite code are subject to independent mathematical assessment.

## References

1. A. Glen, B. V. Halldórsson, S. Kitaev, *Crucial words for abelian powers*, arXiv:0812.4730, first public version 2008-12-27. https://arxiv.org/abs/0812.4730
2. A. Glen, B. V. Halldórsson, S. Kitaev, *Crucial abelian k-power-free words*, Discrete Mathematics and Theoretical Computer Science **12**(5) (2010), 83–96, DOI:10.46298/dmtcs.513. https://dmtcs.episciences.org/513/pdf
3. A. Aberkane, J. D. Currie, N. Rampersad, *The Number of Ternary Words Avoiding Abelian Cubes Grows Exponentially*, Journal of Integer Sequences **7** (2004), Article 04.2.7. https://cs.uwaterloo.ca/journals/JIS/VOL7/Currie/currie18.pdf
