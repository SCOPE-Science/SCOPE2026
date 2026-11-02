# Exact maximal period of ternary order-five orientable sequences

## Finding

Let \(M_3(5)\) be the greatest period of a cyclic word over \(\{0,1,2\}\) in which all cyclic factors of length five are distinct from one another and from every other's reversal (including their own reversals). Then

\[
\boxed{M_3(5)=93.}
\]

The upper bound is proved by an explicit, finite, integer-valued potential certificate on the order-four ternary de Bruijn digraph. A 93-symbol cyclic witness supplies equality:

```
000011200012212010111201211020021210010120010220210020211212201100221111021020221011222012222
```

## Assumptions and scope

Words are indexed cyclically. An orientable sequence of order five has some positive period \(m\), and every cyclic five-symbol window \(w_i\) must be different from \(w_j\) and \(w_j^R\) for any two positions with \(i\ne j\). For \(i=j\), it must also satisfy \(w_i\ne w_i^R\); palindromic five-windows are forbidden. The period counted here is the least period. The alphabet consists of exactly the three available symbols, though a sequence may use a subset.

For any word \(x\), let \(p(x)\) be its *first-occurrence normalization*: on scanning from the left, replace the first new symbol by 0, the second by 1, the third by 2. Define \(r(w)=\min_{\mathrm{lex}}\{p(w),p(w^R)\}\). A missing lookup-table entry below has value zero.

## Proof

**1. Eulerian constraints.** Let \(E\) be the set of the \(m\) distinct cyclic five-windows. The length-four prefix and suffix of a window are its tail and head in the order-four de Bruijn digraph. Since the windows form a closed directed walk, each four-symbol vertex \(v\) has equal indegree and outdegree in \(E\). No palindrome lies in \(E\), and \(E\) meets each nonpalindromic reversal pair in at most one member.

**2. A special vertex cut.** There are exactly six four-symbol palindromes of the form \(v=abba\) with \(a\ne b\). The three nonpalindromic edges entering such a vertex are paired by reversal with the three nonpalindromic edges leaving it; the two sets are disjoint. Reversal exclusion gives \(d^-(v)+d^+(v)\le3\), while balance gives \(d^-(v)=d^+(v)\). Hence

\[
\sum_{v\colon v=abba,\ a\ne b} d^-(v)\le6.
\]

**3. Universal rational dual certificate.** Define \(H(v)=h(p(v))\) and \(Y(w)=y(r(w))\) by these explicit *integer* tables (weights are six times the rational dual weights):

| Pattern \(p(v)\) | \(h\) |
|:---|---:|
| `0001` | -6 |
| `0012` | -1 |
| `0102` | -3 |
| `0110` | -6 |
| `0111` | 6 |
| `0121` | 3 |
| `0122` | 1 |

| Reversal type \(r(w)\) | \(y\) |
|:---|---:|
| `00001` | 12 |
| `00012` | 1 |
| `00101` | 6 |
| `00102` | 9 |
| `00112` | 6 |
| `00120` | 5 |
| `00121` | 2 |
| `00122` | 4 |
| `01002` | 6 |
| `01012` | 9 |
| `01021` | 3 |
| `01102` | 1 |
| `01112` | 18 |
| `01120` | 7 |
| `01201` | 6 |

For **each** of the 216 nonpalindromic ternary five-words \(w\), with prefix \(u\) and suffix \(v\), the following inequality holds:

\[
6\le y(r(w))+12\mathbf 1_{\{v=abba,\ a\ne b\}}+H(v)-H(u).

\]

This is an *exhaustive finite lemma*, not a heuristic numerical assertion: the complete, standard-library-only verifier `verify_certificate.py` below enumerates all \(3^5=243\) words, excludes all 27 palindromes, and checks the 216 inequalities exactly with integers. The other part of the certificate is the exact total weight over all 108 reversal pairs:

\[
\sum_{\{w,w^R\}}y(r(w))=486.

\]

For transparent independent replication, the verifier also constructs the 20 normalized reversal-pair types and counts each type's multiplicity; summing their weights yields 486. Both tables, the pair-sum, and all inequalities appear directly in the package, with no optimization library, floating-point arithmetic, or undocumented input.

Sum the displayed edge inequality over \(E\). The total potential telescopes to zero by degree balance. Reversal exclusion bounds the total \(y\)-contribution by 486, because all \(y\)-weights are nonnegative and at most one edge of each reversal pair occurs. The special-vertex cut bounds the second contribution by \(12\cdot6=72\). Consequently

\[
6m\le486+72=558,\qquad m\le93.
\]

**4. Sharpness.** Let \(s\) be the displayed length-93 word. For all indices \(0\le i<93\), form the circular window \(s_i s_{i+1}s_{i+2}s_{i+3}s_{i+4}\), with subscripts modulo 93. Direct exact enumeration (included in `verify_certificate.py`) checks that these 93 windows are pairwise distinct, none equals its reversal, and no one equals the reversal of any other. Hence \(m\ge93\). All these windows are distinct, so the cyclic word cannot have a smaller period. Together with the upper bound, this proves the theorem.

## Verification

Run `python3 verify_certificate.py` from the directory containing that file. It requires Python's standard library only, and outputs the exact integer certificate checks recorded in `verification_output.txt`. The proof of the universal bound is reduced to 216 explicitly enumerable inequalities, 108 explicitly enumerable pair weights, and six vertex-cut checks. It is a complete finite proof for the fixed parameters, not a sample or an estimate.

## Relationship to prior work

Mitchell and Wild (2025, arXiv:2507.02526v1), their Table 7, reported a ternary order-five construction of length 93, but their upper bound was 99 and their conclusion listed remaining gaps for orders greater than four. The present theorem preserves their 93 lower bound (also independently witnessed above) and closes the missing six-unit upper gap using a sharper vertex-restricted potential certificate. Gabrić and Sawada (2024, arXiv:2407.07029v1) developed asymptotically optimal alphabet-general cycle-joining constructions and established exact maxima in order two; that framework does not give the sharp upper bound \(M_3(5)\le93\).

## Limitations

This establishes only the ternary order-five maximum. It does not classify all maximizers, give a general method for larger orders or alphabets, or assert that no earlier unindexed proof exists. The new upper bound is independently established by the displayed exhaustive certificate, while the prior best construction of length 93 is explicitly attributed.

## References

1. Chris J. Mitchell and Peter R. Wild, *New orientable sequences*, arXiv:2507.02526v1 (2025-07-03), https://arxiv.org/html/2507.02526v1, especially §2, §3, Table 7 and §7.
2. Daniel Gabrić and Joe Sawada, *Constructing k-ary Orientable Sequences with Asymptotically Optimal Length*, arXiv:2407.07029v1 (2024-07-09), https://arxiv.org/html/2407.07029v1, especially §3 and §6.
