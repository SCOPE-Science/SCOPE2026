# The complete terminal curling-transform image of ternary overlap-free words

## Finding

Write \(\Sigma=\{0,1,2\}\). Let \(\mathcal E\) consist of all words \(w\in\Sigma^{84}\) for which both \(w\) and its *direct-prefix curling-number transform* \(C(w)\) are overlap-free. If \(H\) is the following explicit word of length \(83\),

```
H = 11211221211212211221211221121221122121121221211221121221122121122112122121121221121
```

then the **entire transform image and its fibers** are

\[
C(\mathcal E)=\{H1,H2\},\qquad
|C^{-1}(H1)\cap\mathcal E|=4032,\qquad
|C^{-1}(H2)\cap\mathcal E|=2016.
\]

In particular, all \(6048\) admissible length-\(84\) source words have the **same first \(83\) curling numbers**. Exactly \(2016\) labeled admissible length-\(83\) words extend to length \(84\). Each one has **all three** symbols as valid final extensions, and exactly one of its three extensions has last curling number \(2\); the other two have last curling number \(1\). There is no admissible length-\(85\) word.

## Assumptions and scope

A finite word is *overlap-free* if it has no factor \(axaxa\), with \(a\) a letter and \(x\) any (possibly empty) word. Index positions from \(0\). The curling number \(\operatorname{cn}(v)\) of a nonempty word \(v\) is the largest integer \(r\ge 1\) such that \(v=uy^r\) for some word \(u\) and nonempty word \(y\). The transform is \(C(w)[i]=\operatorname{cn}(w[0..i])\), for \(0\le i<|w|\), **without an artificially prepended initial symbol**. No assertion is made for a different convention or for larger alphabets.

An overlap-free word has no cube, so every prefix curling number is \(1\) or \(2\). Its next curling number is \(2\) precisely when its newly extended prefix ends in a square \(yy\) with \(y\ne\epsilon\).

## Proof

The finite proof is an exhaustive induction with two independently implemented transition tests. Define \(\mathcal S_0=\{(\epsilon,\epsilon)\}\), where a pair records a source prefix and its transform. Given a pair \((w,c)\in\mathcal S_{n-1}\) and \(a\in\Sigma\), form \(v=wa\). Discard \(v\) if it has a terminal overlap, i.e., some suffix of length \(2p+1\), \(1\le p\le\lfloor(n-1)/2\rfloor\), has period \(p\). Otherwise append to \(c\) the digit \(d=2\) if \(v\) has a square suffix, and \(d=1\) otherwise. Retain \((v,cd)\) precisely if \(cd\) has no terminal overlap. These tests are implemented by literal comparisons of the indicated finite substrings.

**Completeness of the recurrence.** Every overlap newly created by adding one symbol must end at that symbol; hence the terminal test is necessary and sufficient when the preceding prefix is overlap-free. The absence of cubes justifies the square-suffix curling-number test. The same terminal-overlap argument applies to the extended transform. By induction, \(\mathcal S_n\) is exactly the set of admissible labeled source prefixes of length \(n\), each paired with its full direct-prefix curling transform. Thus an empty \(\mathcal S_{85}\) excludes every admissible longer word by prefix heredity.

**Symmetry reduction.** Any permutation of the three source letters preserves equality of substrings, overlaps, square suffixes, and hence the entire curling transform. The first implementation therefore restricts first symbol occurrences to the canonical order \(0,1,2\). It enumerates all such representative states, not a sample. It finds \(840\) canonical valid words of length \(83\), exactly \(1008\) at length \(84\), and none at length \(85\). Every canonical length-\(84\) word uses all three symbols and thus belongs to a relabeling orbit of size \(3!=6\). Their full count is therefore \(1008\cdot6=6048\).

The \(1008\) canonical terminal states have exactly \(336\) distinct length-\(83\) source parents. Every parent has precisely the three children ending in \(0\), \(1\), and \(2\). Each parent's children have final curling digits with multiset \(\{1,1,2\}\). Direct evaluation of their transforms finds exactly two strings: \(H1\), occurring \(672\) times canonically, and \(H2\), occurring \(336\) times canonically. Therefore each parent has two \(H1\) children and one \(H2\) child. Multiplying by six gives the claimed \(2016\) labeled parents and the two stated fiber cardinalities. This proves the image, the common-prefix rigidity, and the terminal branching classification.

**Independent unquotiented check.** A second implementation searches all three labeled letters without symmetry normalization and uses explicit character-by-character periodicity tests rather than Python substring equality. It directly obtains \(|\mathcal S_{83}|=5040\), \(|\mathcal S_{84}|=6048\), and \(|\mathcal S_{85}|=0\), the same two \(84\)-digit transforms and their fibers, and the all-three-extension property for exactly \(2016\) distinct length-\(83\) parents. The executable complete searches and their outputs are supplied with this result; this is an exact finite proof, not extrapolation from experiments at smaller lengths.

## Verification

With Python 3 standard library, execute `python3 verify_profile.py`. With a C++17 compiler, execute `c++ -std=c++17 -O2 crosscheck_full.cpp -o check_full && ./check_full`. Both programs assert every claimed count, output image, common prefix, and branching property. `computation_output.txt` records their successful outputs. No external datasets, symbolic packages, or other files are needed. The independent C++ check enumerates every admissible *labeled* word at every length through \(85\), whereas the Python check enumerates the exact relabeling quotient; agreement does not rely on copying the first program's candidate list.

## Relationship to prior work

Caveney, Dong, and Shallit (2026), Theorem 7, establish the maximum ternary admissible length \(84\), give the total \(6048\), and display one transformed example. Their Appendix B describes independent full-prefix enumeration for terminal *counts*. The image's exact two-word support, its fiber sizes, its common \(83\)-digit prefix, and the universal three-way final branching are additional statements: knowing only the maximum length and total number of sources does not determine them. The foundational literature of Chaffin, Linderman, Sloane, and Wilks (2013) concerns curling-number statistics and extensions of arbitrary sequences, not this doubly overlap-free terminal family.

## Limitations

The result is a complete **finite boundary classification** for the specified length, not a formula for every shorter-length fiber or a structural classification of every individual source word. The proof's exhaustive numerical steps are finite and explicitly reproducible, but no claim is made about an independently conducted mathematical review, historical uniqueness across all unindexed work, or other curling-number transform conventions.

## References

1. Geoffrey Caveney, Haoxuan Dong, Jeffrey Shallit, *Repetition Avoidance in Curling-Number Transforms*, arXiv:2608.15670v1 (first publicly submitted 2026-08-16), especially §§2.1–2.3 and 4.1 and Appendix B. https://arxiv.org/abs/2608.15670
2. Benjamin Chaffin, John P. Linderman, N. J. A. Sloane, Allan R. Wilks, *On Curling Numbers of Integer Sequences*, Journal of Integer Sequences **16** (2013), Article 13.4.3. https://arxiv.org/abs/1212.6102
