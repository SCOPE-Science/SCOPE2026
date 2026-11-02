# A free two-generator sector of three-bounded prefix duplication

## Finding

For any binary word \(s\) beginning with `010`, consider the one-sided bounded prefix-duplication operation \(\operatorname{PD}_3\): in one step, prepend a nonempty prefix of the current word of length at most three. Write \(\mathcal R_3(s)\) for the set of words reachable from \(s\), including \(s\) itself, and \(d_3(s,t)\) for the minimum number of steps when \(t\) is reachable.

**Theorem (exact normal form and unique derivations).** For every such \(s\),
\[
\{t\in\mathcal R_3(s):t\text{ begins with }01\}
= (01\mid010)^*s.
\]
Every word on the right has **exactly one** derivation from \(s\), not merely one shortest derivation, and
\[
 d_3(s,t)=|t|_1-|s|_1,
\]
where \(|w|_1\) counts the occurrences of `1` in \(w\). In particular, if \(a_{m,r}\) counts these descendants with length increment \(m\) and derivation length \(r\), then
\[
\boxed{\sum_{m,r\geq0}a_{m,r}z^m u^r
=\frac{1}{1-uz^2-uz^3},\qquad
 a_{m,r}=\begin{cases}\binom r{m-2r}&0\leq m-2r\leq r,\\0&\text{otherwise.}\end{cases}}
\]
Thus the exact growth series is universal over all binary seeds with prefix `010`.

**Fibonacci consequence.** With \(F_0=0\), \(F_1=01\), \(F_j=F_{j-1}F_{j-2}\) for \(j\geq2\), and \(f_0=0\), \(f_1=1\), \(f_j=f_{j-1}+f_{j-2}\), every pair of indices \(j\geq i\geq2\) of the same parity has one and only one \(\operatorname{PD}_3\) derivation, of length
\[
\boxed{d_3(F_i,F_j)=f_j-f_i.}
\]
The bound three is a sharp boundary for this uniqueness structure: at duplication bound four the word `010101010` has a two-step derivation from `010` although its three-bounded distance is three, and the prefix-`01` reachable language itself becomes strictly larger.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\). A prefix duplication is \(w\mapsto pw\) with \(1\leq |p|\leq 3\) and \(p\) a prefix of \(w\); suffix duplication and internal duplication are not allowed. The theorem concerns the reachable descendants beginning with `01`, not the entire reachable language. The initial word \(s\) may contain arbitrary later symbols, but its first three symbols must be `010`. A derivation is a finite ordered sequence of these legal operations, with the empty derivation allowed. Formal generating functions count distinct target words or, equivalently here, their unique derivations.

## Proof

**1. An absorbing prefix.** A word beginning with `00` retains prefix `00` after every prefix duplication of positive length: a duplicated prefix of length one contributes `0` before the old leading `0`, and a prefix of length two or three already begins with `00`. From a word beginning `010`, a length-one duplication produces a word beginning `00`. Consequently no derivation ending at a word beginning `01` can ever use a length-one step.

**2. Exactly two admissible transitions in the surviving sector.** A current word beginning `010` has length-two prefix `01` and length-three prefix `010`. Prepending either yields a word that still begins `010`. Inductively, every derivation from \(s\) that ends with prefix `01` consists entirely of those two steps. Conversely, every finite sequence of those two steps is legal. Thus its target is exactly a word of \((01\mid010)^*s\), establishing the normal-form equality.

**3. Uniqueness.** Each of the blocks `01` and `010` contains exactly one `1`, in its second position, and \(s\) also begins with `01`. Given \(t=b_1\cdots b_rs\), with each \(b_j\) one of those two blocks, the successive distances between the `1` in \(b_j\) and the next `1` (in \(b_{j+1}\), or in \(s\) if \(j=r\)) are exactly \(|b_j|\in\{2,3\}\). These distances can be read unambiguously from the final word and the specified suffix \(s\). They determine \(b_1,\ldots,b_r\) uniquely. The chronological duplication order is the reverse of this left-to-right block order. No length-one step can occur by Step 1, hence no alternative derivation is possible.

**4. Exact distances and enumeration.** Each permissible step in this sector prepends one `1`, so every path to \(t\) has exactly \(|t|_1-|s|_1\) steps. Uniqueness proves this is the distance. A block `01` contributes length two and one step, while `010` contributes length three and one step. Summing over ordered sequences of blocks gives \(\sum_{r\geq0}(u z^2+u z^3)^r=(1-u z^2-u z^3)^{-1}\). With \(r\) blocks, the number having length increment \(m\) is the number of choices of \(m-2r\) length-three blocks among \(r\), proving the coefficient formula.

**5. Fibonacci pairs.** The recurrence implies that \(F_j\) ends in \(F_{j-2}\); consequently, \(F_i\) is a suffix of \(F_j\) whenever \(j\geq i\) and their indices have the same parity. Each \(F_i\) for \(i\geq2\) begins `010`. The identity \(F_i=\phi^i(0)\) for \(\phi(0)=01\), \(\phi(1)=0\), shows that every \(F_i\) avoids `11` and `000`: images of adjacent letters cannot give consecutive `1` symbols, and a run of three `0` symbols would require consecutive original `1` symbols, which do not occur. The first `1` is always at the second position. Therefore the gaps between consecutive `1` symbols are two or three. As \(F_j\) begins `01` and ends in \(F_i\), all the gaps before the specified suffix decompose the preceding prefix uniquely into `01` and `010` blocks. The normal-form theorem applies. Finally, \(|F_i|_1=f_i\), since the number of `1` symbols satisfies the Fibonacci recurrence with initial values zero and one. This proves the displayed distance formula and uniqueness.

**6. Sharp change at bound four.** The two valid derivations

`010 → 01010 → 010101010` (prefix lengths two, four), and

`010 → 01010 → 0101010 → 010101010` (three prefix-length-two steps)

show that the first target has distance two at bound four, versus three at bound three. One step at bound four cannot add six symbols. Also `010 → 010010 → 0100010010` (prefix lengths three, four) reaches a word beginning `01` containing `000`. No word of \((01\mid010)^*010\) contains `000`; hence the prefix-`01` language at bound four is strictly larger. Both assertions are exact.

## Verification

Run `python3 verify.py` with standard-library Python 3. The program independently (a) constructs all derivations, including duplications that leave the prefix-`01` sector, for five seeds through nineteen added symbols; (b) compares the observed sector, path multiplicities, distance and complete bivariate counting coefficients with the theorem; (c) computes distances and shortest-path multiplicities again by a separate reverse-suffix dynamic program for all 63 same-parity Fibonacci pairs through index sixteen; and (d) checks both bound-four witnesses. The recorded output is in `verification_output.txt`. These finite tests corroborate, but do not replace, the proofs for arbitrary lengths and indices.

## Relationship to prior work

Cabrera Salamanca and Smith (arXiv:2607.20405, first submitted 22 July 2026) proved reachability of same-parity Fibonacci words by three-bounded prefix duplications, with a recursive construction; their paper explicitly says that the displayed construction does not minimize step count. Its companion repository describes an optimized shortest-derivation program for Fibonacci inputs, but does not state this general exact prefix-sector normal form, the uniqueness theorem, the universal distance enumerator, or the closed all-pairs Fibonacci formula. The companion code therefore provides related computational coverage of the Fibonacci special case, which is not claimed here as an isolated independent discovery. The new theorem concerns arbitrary binary seeds beginning `010` and characterizes all paths in an entire naturally invariant sector.

García López, Manea and Mitrana (2014) introduced general prefix/suffix duplication distances and efficient algorithms. Dumitran, Gil, Manea and Mitrana (2014; expanded 2015) studied bounded prefix/suffix duplication and regular-language closure. These general algorithms and closure results do not, from the accessible descriptions, establish this specific free two-generator sector or uniqueness. Full-text access to the bounded-duplication paper was incomplete; the residual priority risk is noted below rather than treated as proof of noncoverage.

## Limitations

The normal form is restricted to one-sided prefix duplication of bound three and targets preserving prefix `01`; it does not classify descendants beginning `00`, suffix-duplication paths, or general bounds. Its Fibonacci corollary covers same-parity indices at least two. The proof shows no assertion of uniqueness for \(k\geq4\). The literature comparison cannot rule out independent unindexed statements or inaccessible full text. No independent mathematical audit has been performed.

## References

1. D. Cabrera Salamanca and T. J. Smith, *Generating Fibonacci Words via the Prefix–Suffix Duplication Operation*, arXiv:2607.20405v1, 22 July 2026. https://arxiv.org/html/2607.20405v1
2. Companion implementation, *Fibonacci-words_Dumitrans-Conjecture_PD*, README and `derive.cpp`. https://github.com/flarelabstfx/Fibonacci-words_Dumitrans-Conjecture_PD
3. J. García López, F. Manea and V. Mitrana, *Prefix–suffix duplication*, Journal of Computer and System Sciences (2014), doi:10.1016/j.jcss.2014.02.011. https://doi.org/10.1016/j.jcss.2014.02.011
4. M. Dumitran, J. Gil, F. Manea and V. Mitrana, *Bounded Prefix-Suffix Duplication*, CIAA (2014), doi:10.1007/978-3-319-08846-4_13. https://oa.upm.es/41500/
