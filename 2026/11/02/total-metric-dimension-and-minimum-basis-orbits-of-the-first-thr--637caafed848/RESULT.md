# Total metric dimension and minimum-basis orbits of the first three open hypercubes

## Finding

Let \(Q_d\) denote the graph with vertex set \(\{0,1\}^d\), where adjacent strings differ in one coordinate. A set \(S\) is *totally resolving* if for every distinct \(u,v\in V(Q_d)\), there exists \(w\in S\setminus\{u,v\}\) such that \(d(u,w)\neq d(v,w)\). Let \(\dim_t(Q_d)\) be the least size of such an \(S\). Then

\[
\dim_t(Q_4)=\dim_t(Q_5)=\dim_t(Q_6)=6.
\]

Furthermore, \(Q_4\) has exactly \(1600\) six-vertex total resolving sets. The entire set of these bases splits into exactly \(11\) orbits under \(\operatorname{Aut}(Q_4)\), with orbit sizes

\[
32,32,96,96,\underbrace{192,192,192,192,192,192,192}_{7\text{ orbits}}.
\]

## Assumptions and scope

The result concerns only the three finite graphs \(Q_4,Q_5,Q_6\); it does not assert a formula for every dimension. Vertices are encoded by integers from \(0\) through \(2^d-1\), with coordinates their binary digits. The graph distance is Hamming distance \(d(u,v)=\operatorname{wt}(u\oplus v)\). A *total* resolving landmark must be different from both vertices being distinguished. All counts concern unordered, labeled vertex subsets (not ordered tuples).

## Proof

**1. Exact separation predicate and parity reduction.** For each unordered pair \(\{u,v\}\), define

\[
B(u,v)=\{w\in V(Q_d)\setminus\{u,v\}:\operatorname{wt}(u\oplus w)\ne\operatorname{wt}(v\oplus w)\}.
\]

Thus \(S\) is totally resolving if and only if \(S\cap B(u,v)\neq\varnothing\) for every such pair. In the Hamming cube, \(d(u,w)+d(v,w)\) has parity equal to \(d(u,v)\); consequently if \(d(u,v)\) is odd, *every* third vertex \(w\) distinguishes the pair. Because all candidate sets below have at least five vertices, odd-distance pairs are automatically covered. It therefore suffices to test even-distance pairs, numbering \(56\), \(240\), and \(992\) in dimensions \(4,5,6\), respectively.

**2. Five-point lower-bound certificate.** Total resolvability is monotone under enlarging a selected set. If some total resolving set had at most five vertices, there would exist one of exactly five vertices. Translation by XOR with any chosen member is a graph automorphism taking that member to integer \(0\); hence there must be a five-set containing \(0\) that satisfies every even-pair separation predicate. The standalone exhaustive verifier enumerates all \(\binom{2^d-1}{4}\) sets containing \(0\): precisely \(1365\) for \(d=4\), \(31465\) for \(d=5\), and \(595665\) for \(d=6\). In each case, **zero** candidates meet the complete separation predicate. The program directly constructs every \(B(u,v)\) from Hamming distances, tests each candidate by bitwise intersection, and asserts these exact exhaustion counts. Therefore \(\dim_t(Q_d)\ge6\) for each of the three dimensions.

**3. Explicit upper-bound certificates.** The following six-vertex subsets, with vertex labels interpreted as binary coordinates, intersect every even-pair separator set and hence totally resolve their cubes:

\[
\begin{aligned}
Q_4 &: \{0,1,2,3,4,5\},\\
Q_5 &: \{0,1,13,14,21,23\},\\
Q_6 &: \{6,15,26,38,55,60\}.
\end{aligned}
\]

The same standalone verifier checks all \(56\), \(240\), and \(992\) even-pair constraints for these exact witnesses, producing no failure. With Step 2 this proves the three equalities.

**4. Complete minimum-basis count in \(Q_4\).** Every six-element vertex subset is examined once using six strictly increasing labels, so the loop covers exactly \(\binom{16}{6}=8008\) subsets. The separation predicate accepts exactly \(1600\). To count symmetry classes, apply all \(16\) XOR translations and all \(4!=24\) permutations of bit coordinates to eleven exhibited representatives:

```text
[0,1,2,3,4,5]       96
[0,1,2,3,4,9]      192
[0,1,2,4,9,10]     192
[0,1,2,5,6,7]       32
[0,1,2,5,6,11]     192
[0,1,2,5,6,12]     192
[0,1,2,5,6,15]     192
[0,1,2,5,10,12]    192
[0,1,2,5,11,12]    192
[0,1,6,7,10,11]     32
[0,1,6,7,10,13]     96
```

XOR translations and coordinate permutations are all cube automorphisms: any automorphism is determined by the image of \(0\) and the permutation induced on its coordinate neighbors; inducting on Hamming weight fixes every remaining vertex. The verifier checks that every representative is a valid base, every generated orbit consists exclusively of bases, no two listed orbits intersect, and their union is **exactly** the independently enumerated \(1600\)-element set. This proves both the orbit sizes and completeness; \(2\cdot32+2\cdot96+7\cdot192=1600\).

The four steps are a finite, exhaustive computer-assisted proof of precisely the stated finite cases. All quantifiers reduce to explicitly bounded loops provided in `verify_total_hypercubes.cpp`.

## Verification

Compile and run the complete standalone verifier with a C++17 compiler:

```sh
g++ -O3 -std=c++17 -Wall -Wextra -pedantic verify_total_hypercubes.cpp -o verify_total_hypercubes
./verify_total_hypercubes
```

Expected decisive output:

```text
n=4 normalized_five_sets_checked=1365 valid=0
n=4 nontrivial_pair_constraints=56 exhibited_six_set_valid=1
n=5 normalized_five_sets_checked=31465 valid=0
n=5 nontrivial_pair_constraints=240 exhibited_six_set_valid=1
n=6 normalized_five_sets_checked=595665 valid=0
n=6 nontrivial_pair_constraints=992 exhibited_six_set_valid=1
Q4_all_six_sets=8008 total_bases=1600
Q4_orbits=11 sizes=32 32 96 96 192 192 192 192 192 192 192
ALL_CHECKS_PASSED
```

The code uses integer bit masks (at most \(64\) vertices) and full loops over all relevant combinations. A missing separator triggers a failed assertion; the absence of such failures alone is not the certificate without inspecting the complete enumeration code.

## Relationship to prior work

Hedetniemi, Laskar, and Mulder introduced this exact third-landmark total-resolvability notion and explicitly asked for the total metric dimension of hypercubes in dimensions exceeding three (their Question 7). They proved the three-cube case, not the three dimensions resolved here. Kelenc and collaborators studied usual vertex, edge, and mixed metric dimension of hypercubes; these allow different categories of distinguished objects or landmarks and do not imply the third-landmark property. Work on *weak total* resolvability imposes a different, weaker quantifier and cannot itself certify this total-resolving census. The structural symmetry and full first-open-case enumeration are additional to the scalar dimension values.

## Limitations

This finding neither supplies a general asymptotic bound nor determines \(\dim_t(Q_d)\) for \(d\ge7\). The lower bounds and exact minimum-basis census are exhaustively finite, not structural inequalities for arbitrary dimensions. Independent mathematical checking has not been performed; a compiler and source inspection are necessary to replay the finite certificate. The literature comparison may have missed a synonymous, unpublished, or inaccessible earlier treatment.

## References

1. S. T. Hedetniemi, R. C. Laskar, H. M. Mulder, *New resolvability parameters of graphs*, AKCE International Journal of Graphs and Combinatorics **17** (2020), 1028–1038. DOI: 10.1016/j.akcej.2019.12.021. First verified public online date: 2020-05-04. Open full text: https://repub.eur.nl/pub/126872/Repub_126872_O-A.pdf.
2. A. Kelenc, A. T. M. Toshi, R. Škrekovski, I. G. Yero, *On Metric Dimensions of Hypercubes*, arXiv:2102.10916 (2021). https://arxiv.org/pdf/2102.10916.
3. K. Casel, A. Estrada-Moreno, H. Fernau, J. A. Rodríguez-Velázquez, *Weak Total Resolvability in Graphs*, Discussiones Mathematicae Graph Theory (2016), DOI: 10.7151/dmgt.1853.
