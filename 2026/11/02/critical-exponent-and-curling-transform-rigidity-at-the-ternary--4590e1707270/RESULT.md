# Critical-exponent and curling-transform rigidity at the ternary nine-fourths boundary

## Finding

Fix the labeled alphabet \(\Sigma=\{0,1,2\}\). A finite word \(w\) is \(\frac94\)-power-free if no nonempty factor has exponent at least \(\frac94\). Write \(C(w)\) for its direct-prefix curling-number transform. Let \(\mathcal F\) be the set of words \(w\in\Sigma^{84}\) such that \(w\) is \(\frac94\)-power-free and \(C(w)\) is overlap-free (contains no factor of exponent greater than \(2\)).

Define the following two binary-output strings, whose letters are `1` and `2`:

```
A = 112112212112122112212112211212211221211212212112211212211221211221121221211212211211
B = 112112212112122112212112211212211221211212212112211212211221211221121221211212211212
```

**Complete joint distribution.** Exactly \(10{,}368\) labeled words lie in \(\mathcal F\), and their only possible curling transforms are \(A\) and \(B\). Their source critical exponents are exactly \(2\) and \(\frac{11}{5}\), with this complete table:

| Maximum exponent in \(w\) | \(C(w)=A\) | \(C(w)=B\) | Total |
|---|---:|---:|---:|
| \(2\) | 4032 | 2016 | 6048 |
| \(\frac{11}{5}\) | 2880 | 1440 | 4320 |
| **Total** | **6912** | **3456** | **10368** |

The two transforms agree at each of their first \(83\) positions and differ only at their last symbol. Thus every extremal source has the same square-ending-prefix pattern through position \(83\), even though \(4320\) sources have exponent strictly greater than \(2\). No source critical exponent occurs strictly between \(2\) and \(\frac{11}{5}\), or strictly between \(\frac{11}{5}\) and \(\frac94\), within \(\mathcal F\).

## Assumptions and scope

Words are linear, their letters belong to the *labeled* three-letter alphabet, and global symbol permutations are **not** identified in the displayed counts. The exponent of a nonempty finite factor is its length divided by its least period. A word is overlap-free precisely when it has no factor of exponent greater than \(2\). The curling number of a nonempty word is the largest integer \(k\) such that its suffix is \(u^k\) for some nonempty word \(u\); \(C(w)[j]\) records the curling number of the prefix through position \(j\). Source \(\frac94\)-power-freeness implies cubefreeness, hence every curling number is `1` or `2`.

## Proof

We give an exact, finite exhaustive proof with two standalone implementations in independent languages. The soundness of the finite algorithm rests on the following elementary reductions.

**1. Suffix reduction for the source.** A new word of length \(n\) remains \(\frac94\)-power-free precisely when its old prefix was valid and there is no positive period \(p\) for which its suffix of length \(L_p=\lceil9p/4\rceil\) has period \(p\). To see sufficiency, any first newly introduced forbidden factor must end at the appended symbol; taking its suffix of length \(L_p\) preserves the period. Necessity is immediate because that suffix has exponent \(L_p/p\ge\frac94\). Only periods with \(L_p\le n\) need be examined. Checking a period does not require it to be the least period: this introduces no false positives, since such a suffix itself already has exponent at least \(\frac94\) relative to a valid period.

**2. Exact curling transform.** Every admissible source is cubefree. A prefix therefore has curling number `2` exactly when it ends in a square \(uu\) and otherwise curling number `1`. The verifier checks every positive square length; this is the exact definition, rather than an approximation to the transform.

**3. Suffix reduction for the transform.** An overlap is a periodic factor with some positive period \(p\) and length \(2p+1\). Hence the transform remains overlap-free after extension if and only if no suffix of length \(2p+1\) has period \(p\), for any such \(p\).

**4. Exhaustive search.** Start with the empty word and extend each valid prefix by each allowed alphabet symbol, applying Steps 1–3. The conditions are prefix-hereditary, so induction proves that the retained set at each length is exactly the desired set of valid prefixes. The C++ verifier follows all three labeled symbols directly. It obtains \(10{,}368\) sources at length \(84\) and none at length \(85\).

**5. Exact exponent classification.** For each terminal word and each possible period \(p\), scan the consecutive matches \(w[i]=w[i+p]\). A run of \(r\) matches yields a factor of length \(p+r\) and period \(p\), of exponent \((p+r)/p\). Maximizing over all runs and periods is exactly the largest exponent, since any periodic factor contributes its corresponding matched run, and taking the least period can only increase the exponent. The verifiers compare fractions by integer cross multiplication or exact rational arithmetic. All \(10{,}368\) words have maximum exponent exactly \(2\) or \(\frac{11}{5}\). Cross-tabulating with the two output strings gives the four integer counts stated above.

**6. Independent symmetry-reduced replay.** The Python verifier uses the restricted-growth canonical representative of each orbit of global alphabet relabelings: after symbols up to \(m\) have appeared, the next symbol is one of \(0,\ldots,\min(2,m+1)\). This gives exactly one representative per orbit. All terminal representatives use three symbols, hence each expands into \(3!=6\) labeled words. This independently obtains \(1728\) representatives with table entries \(672,336,480,240\), agreeing with the C++ full-alphabet counts after multiplication by six.

These algorithms exhaust every candidate under the definitions and have no unexamined search branches. Their correctness does not rely on a numerical optimization solver, randomized sampling or extrapolation from test lengths.

## Verification

Extract `verify.py` and `verify_full.cpp` from this package and run `python3 verify.py` and `c++ -O3 -std=c++17 verify_full.cpp -o verify_full && ./verify_full`. Both use only standard libraries and print `POWER94_CURLING_CANONICAL_VERIFY_OK` and `POWER94_CURLING_LABELED_VERIFY_OK` respectively. The Python verification additionally recomputes every terminal transform from scratch. The C++ verification enumerates all labeled sources without symmetry reduction and recomputes exact critical exponents.

## Relationship to prior work

Caveney, Dong and Shallit (2026), Theorem 9, establish that precisely \(10{,}368\) sources satisfy the two conditions at length \(84\), and none do at length \(85\). Their Theorem 7 treats the *stricter* subclass in which the source is itself overlap-free; this contains \(6048\) words. The present finding is not a new maximum-length or total-count result: it determines the previously unstated complete **joint distribution of the source's critical exponent and the curling transform** for all \(10{,}368\) words. The extra \(4320\) sources form a single, exact \(\frac{11}{5}\)-critical stratum, and the full class has only two transforms. Earlier classifications restricted to overlap-free sources cannot imply these facts for the additional \(4320\) sources.

## Limitations

The theorem is an exhaustive finite classification at length \(84\) for the *non-strict* \(\frac94\)-power-free condition. It does not classify arbitrary lengths, arbitrary alphabets, or source exponents allowing equality at \(\frac94\). Its exactness relies on straightforward finite programs whose mathematical search reductions are described above; no separate proof of a closed-form formula for arbitrary lengths is claimed. Formal independent mathematical auditing and definitive historical-priority assessment have not been performed.

## References

- G. Caveney, H. (Jason) Dong, and J. Shallit, *Repetition Avoidance in Curling-Number Transforms*, arXiv:2608.15670v1, first made public August 16, 2026. https://arxiv.org/abs/2608.15670 . Especially Sections 2 and 4, Theorems 7 and 9, and Appendix B.
- F. J. van de Bult, D. C. Gijswijt, J. P. Linderman, N. J. A. Sloane, and A. R. Wilks, *A slow-growing sequence defined by an unusual recurrence*, Journal of Integer Sequences 10 (2007), Article 07.1.2 (background on curling numbers).
