# Equality classification for binary length-seven frameproof codes

## Finding
Let \(C\subseteq\{0,1\}^7\) be a binary \(2\)-frameproof code: for every coalition \(P\subseteq C\) with \(|P|\le 2\), the descendant of \(P\) contains no codeword outside \(P\). Then

\[
|C|\le 9.
\]

Exactly \(107{,}520\) unordered labeled codes attain equality. Under the full Hamming-isometry group \((C_2)^7\rtimes S_7\), of order \(645{,}120\), the maximum codes form exactly two orbits. Their sizes are \(80{,}640\) and \(26{,}880\), so the corresponding stabilizer orders are \(8\) and \(24\).

Representatives are:

```text
0000000  0000011  0001101  0110001  0111110  1010101  1011010  1100110  1101001
```

and

```text
0000000  0000111  0011001  0011110  0101010  0101101  0110011  1001011  1110100
```

For the first orbit, the numbers of unordered pairs at Hamming distances \(2,3,4,5\) are respectively \(1,10,17,8\); every coordinate splits the nine codewords as \(4+5\). For the second orbit, the numbers of pairs at Hamming distances \(3,4,5,6\) are respectively \(15,17,3,1\); one coordinate splits as \(2+7\) and the other six split as \(4+5\). These invariants separate the two equality types.

## Assumptions and scope
For binary words \(x,y,z\), the word \(z\) lies in the descendant of \(\{x,y\}\) exactly when, in every coordinate where \(x\) and \(y\) agree, \(z\) has the same symbol. In the binary Hamming cube this is equivalent to \(z\) lying on a shortest \(x\)-to-\(y\) path. Thus binary \(2\)-frameproof codes are the same finite objects as binary \((2,1)\)-separating systems and general-position sets in the seven-dimensional hypercube. The claim concerns unordered subsets of the labeled cube; equivalence is taken only under coordinate permutations and independent binary symbol swaps, i.e. Hamming isometries.

## Proof
For distinct words \(a,b,c\), call the triple bad if one word lies on a shortest path between the other two. The verifier constructs, for every unordered pair \(a,b\), the exact bit mask of all third words \(c\) that make a bad triple. It then performs an increasing-order depth-first enumeration of codes containing `0000000`. When a new word \(v\) is selected, every still-available word that would make a bad triple with \(v\) and any previously selected word is removed. Inductively, every visited partial code is valid. Conversely, a valid increasing extension is never removed, because removing it would exhibit a forbidden triple. Hence the search is exhaustive rather than heuristic.

Every nonempty binary code can be translated by one of its words so that it contains `0000000`, and translation preserves the frameproof property. The exhaustive normalized search finds exactly \(7{,}560\) valid nine-word codes containing `0000000` and no valid ten-word code containing `0000000`. Therefore the exact maximum is \(9\).

For a nine-word code, no nonzero translation can stabilize the set: a nonzero translation is a fixed-point-free involution and would partition a stabilized set into pairs, impossible for odd cardinality. Hence each translation orbit has \(128\) members and exactly \(9\) of them contain `0000000`, one for each choice of translated codeword. Therefore the total number of labeled maximum codes is

\[
7{,}560\cdot\frac{128}{9}=107{,}520.
\]

Finally, the verifier explicitly generates all \(7!\) coordinate permutations. For each normalized maximum it closes under coordinate permutations and then translates each resulting code by each of its nine words back to a code containing `0000000`. The \(7{,}560\) normalized maxima split into classes of sizes \(5{,}670\) and \(1{,}890\). Multiplying by \(128/9\) gives full Hamming-isometry orbit sizes \(80{,}640\) and \(26{,}880\). Orbit-stabilizer then gives stabilizer orders \(8\) and \(24\). Direct pair-distance and coordinate counts give the stated distinguishing profiles.

## Verification
`artifacts/verify_q7_frameproof.py` is a standalone Python verifier using only the standard library. It reconstructs all \(128\) vertices and all forbidden triples from the definition; exhaustively enumerates target sizes \(9\) and \(10\) after translation normalization; directly rechecks every enumerated maximum; reconstructs the full \(645{,}120\)-element Hamming-isometry action from translations and the \(7!\) coordinate permutations; and checks both equality profiles.

A fresh run produced:

```text
VERIFY_OK vertices=128 maximum=9 origin_maxima=7560 target10=0 labeled_maxima=107520 natural_group=645120 orbits=2 orbit_sizes=80640,26880 stabilizers=8,24 nodes9=2986961 nodes10=2029645 normalized_sha256=e5e0083ce6ccf2c55968c0f4b5866679183ceb50474b1da5d518f17c49eb6228
ORBIT 1 rep=0000000,0000011,0001101,0110001,0111110,1010101,1011010,1100110,1101001 normalized_origin=5670 full_size=80640 stabilizer=8 distance_profile=2x1,3x10,4x17,5x8 coordinate_profiles=4-5,4-5,4-5,4-5,4-5,4-5,4-5
ORBIT 2 rep=0000000,0000111,0011001,0011110,0101010,0101101,0110011,1001011,1110100 normalized_origin=1890 full_size=26880 stabilizer=24 distance_profile=3x15,4x17,5x3,6x1 coordinate_profiles=2-7,4-5,4-5,4-5,4-5,4-5,4-5
```

`artifacts/verification_output.txt` records this output verbatim.

## Relationship to prior work
Stinson and Wei developed the combinatorial frameproof-code formulation in the fingerprinting setting; the inspected bibliographic record assigns MSC \(94A60\). Randriambololona states the equivalent binary \((2,1)\)-separating/no-three-between formulation. Korže and Vesel explicitly identify the hypercube general-position problem with binary \((2,1)\)-separating systems and report exact general-position numbers through dimension seven, but their inspected article reports cardinalities rather than an equality-case census. OEIS A089676 records the value \(9\) in dimension seven together with a Bevan witness, again without a labeled count or orbit classification.

A closely related published-finding corpus record determines the exact value \(10\) in dimension eight and describes that case as the first dimension beyond the previously known exact range through dimension seven. Its full result text does not classify the dimension-seven equality cases. Exact-parameter, alias, representative, orbit-size, and stabilizer searches found no inspected statement implying the count \(107{,}520\) or the two-orbit decomposition. Thus the finding is a structural refinement of a known exact cardinality, not a new claim about the already-known value alone.

## Limitations
The equality classification is finite and computer-assisted; it does not by itself give a closed-form classification in higher dimensions. Originality is assessed against the inspected primary literature, the cited database entry, the related published-finding corpus record, and exact-parameter/structural searches. The exact Bevan source underlying the OEIS small-dimensional witness was not located as a primary full text, so an obscure historical equality-case enumeration remains a residual risk. An earlier 1995 paper by Körner is relevant to the asymptotic Hamming-space problem, but the inspected metadata exposed only month-level publication dating; no artificial day has been assigned from that source.

## References
1. D. R. Stinson and R. Wei, “Combinatorial Properties and Constructions of Traceability Schemes and Frameproof Codes,” *SIAM Journal on Discrete Mathematics* 11 (1998), 41–53. DOI: 10.1137/S0895480196304246.
2. H. Randriambololona, “(2,1)-Separating systems beyond the probabilistic bound,” *Israel Journal of Mathematics* 195 (2013), 171–186; arXiv:1010.5764.
3. D. Korže and A. Vesel, “General Position Sets in Two Families of Cartesian Product Graphs,” *Mediterranean Journal of Mathematics* 20 (2023), article 203. DOI: 10.1007/s00009-023-02416-z.
4. OEIS A089676, maximal acute/no-between subsets of the binary cube, including the dimension-seven value and witness.
5. “Exact size of binary (2,1)-separating systems of length eight,” published-finding corpus record `2026/9/21/SCOPE-exact-length-eight-binary-21-separating-systems--bbbd20b813f0`.
