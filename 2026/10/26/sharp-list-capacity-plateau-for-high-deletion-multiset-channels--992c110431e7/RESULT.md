# Sharp list-capacity plateau for high-deletion multiset channels

## Finding

**Theorem.** For all integers \(q\ge3\), \(k\ge2\), and \(2\le L\le k\), the optimal size of a \(q\)-ary unordered multiset code correcting exactly \(n-k\) deletions with decoding list size at most \(L\) satisfies

\[
M_{q,k,L}(n)=\begin{cases}qL+1,&n=q(k-1),\\qL,&n\ge q(k-1)+1.\end{cases}
\]

At the boundary, every maximizing code contains the unique multiset \((k-1,\ldots,k-1)\), and all other codewords have exactly one coordinate of multiplicity at least \(k\). Beyond the boundary, every maximizing codeword has exactly one such coordinate. In both regimes precisely \(L\) codewords have their unique high-multiplicity coordinate at each symbol.

The loss of exactly one admissible message after crossing the stated threshold is sharp, uniform in all three parameters, and attained by a constructive cyclic code.

## Assumptions and scope

Let \(\Sigma=\{0,\ldots,q-1\}\). A transmitted multiset is identified with \(x=(x_0,\ldots,x_{q-1})\in\mathbb{Z}_{\ge0}^{q}\) of total multiplicity \(|x|=n\). An exactly \(n-k\)-deletion output is a vector \(y\in\mathbb{Z}_{\ge0}^{q}\) of total multiplicity \(|y|=k\) with \(y_i\le x_i\) for every coordinate. A code \(\mathcal C\) has **list bound** \(L\) when

\[
\forall y\in\mathbb Z_{\ge0}^{q},\quad |y|=k:\quad |\{x\in\mathcal C:y\le x\}|\le L.
\]

The optimal cardinality under this condition is \(M_{q,k,L}(n)\). Only distinct multiset codewords are counted (not their ordered permutations). The theorem is about exactly \(n-k\) symbol deletions, not ordered subsequences; in this fixed-length setting, successful decoding with up to \(n-k\) deletions follows from the same condition by first discarding additional received symbols.

## Proof

**1. A universal incidence bound.** Call a coordinate \(i\) *heavy* in \(x\) if \(x_i\ge k\). The received monochromatic multiset \(k e_i\) is a descendant of every word heavy in \(i\). Therefore at most \(L\) codewords in an admissible family are heavy in any particular coordinate. Consequently, summing heavy-coordinate incidences gives

\[
\sum_{i=0}^{q-1}|\{x\in\mathcal C:x_i\ge k\}|\le qL.
\]

If \(n\ge q(k-1)+1\), every vector of sum \(n\) is heavy in some coordinate, by the pigeonhole principle. Each codeword contributes at least one incidence, hence \(|\mathcal C|\le qL\).

At \(n=q(k-1)\), the only vector without a heavy coordinate is

\[
F=(k-1,k-1,\ldots,k-1).
\]

Thus \(|\mathcal C|\le qL+1\). These conclusions do not assume any symmetry or linearity of the code.

**2. Explicit cyclic witnesses.** Interpret alphabet indices modulo \(q\). For every \(n\ge q(k-1)\), \(i\in\Sigma\), and \(0\le j<L\), define

\[
X_{i,j}=(n-j)e_i+j e_{i+1\bmod q}.
\]

Because \(j\le L-1\le k-1\) and \(n-j\ge(q-1)(k-1)\ge k\) for \(q\ge3\), \(X_{i,j}\) is heavy in \(i\) and not in any other coordinate. The \(qL\) vectors \(X_{i,j}\) are pairwise different.

Write \(\mathcal C_0=\{X_{i,j}:i\in\Sigma,\ 0\le j<L\}\). For a fixed \(i\), at most \(L\) of its words can contain any given received multiset. Two different index groups cannot share a received multiset of size \(k\): their word supports lie on two distinct edges of the directed simple cycle on \(q\ge3\) vertices, which intersect in at most one symbol. Any common received multiset would therefore have to be monochromatic, say \(k e_a\). But that symbol appears with multiplicity less than \(k\) on the **tail** side of one of the two edges, a contradiction. Hence each received multiset occurs in at most one group and has at most \(L\) parent codewords. Thus \(\mathcal C_0\) is valid for all \(n\ge q(k-1)\), attaining \(qL\).

For exactly \(n=q(k-1)\), add \(F\). No monochromatic received multiset is a descendant of \(F\), since each coordinate of \(F\) is \(k-1\). Every output \(y\le F\) can consequently be a descendant of **at most** \(L-1\) codewords from \(\mathcal C_0\): the unique possibly contributing group contains the word \(X_{i,0}=n e_i\), which has only monochromatic descendants and therefore does not contain \(y\). The addition of \(F\) raises the number of parents of any receiver to at most \(L\). We have constructed a valid code of \(qL+1\) words at the boundary.

The bounds and constructions prove both exact formulas.

**3. Rigidity of every optimum.** If equality \(|\mathcal C|=qL\) holds above the boundary, the total number of heavy-coordinate incidences is at least \(|\mathcal C|=qL\) and at most \(qL\). Therefore each codeword has exactly one heavy coordinate and each of the \(q\) coordinates is heavy in exactly \(L\) codewords. If \(|\mathcal C|=qL+1\) at the boundary, then \(F\) must be present, as the only possible non-heavy word. Removing it leaves \(qL\) heavy words, and the same equality argument proves exactly the stated profile. \(\square\)

## Verification

Run `python3 verify.py` with Python 3 standard library; expected final line is `ALL_CHECKS_PASS`. The checker verifies the cyclic code, its cardinality, the parent-list condition for all received vectors, and the heavy-coordinate structure over \(54\) parameter/length cases (covering \(1,563\) tested receiver vectors). It also computes the actual exhaustive optimum across *all* codes in two small cases: \((q,k,L,n)=(3,2,2,3)\) and \((3,2,2,4)\), obtaining \(7\) and \(6\) respectively. The bound for all parameters is the complete symbolic proof above, not a finite-data inference.

## Relationship to prior work

Kreindel, Essayag, and Zabokritskiy's 2026 multiset-deletion paper defines the same unordered multiplicity-vector channel, studies **unique** decoding, gives cyclic constructions and upper bounds, and determines several high-deletion special cases. Its exact results for fixed survivor sizes concern list size one; the present result concerns every \(2\le L\le k\) and describes a different sharp one-message loss together with an extremal heavy-coordinate profile. The classical Kovačević–Tan paper develops lattice/Sidon-code methods for multiset permutation channels, again in the unique-decoding setting. List-decodable deletion results for *ordered* strings (e.g. Lin 2026) concern subsequences and do not imply the present multiset capacities.

## Limitations

No formula is asserted here for \(q=2\), \(L=1\), \(L>k\), or \(n<q(k-1)\). The heavy-coordinate profile classifies a necessary feature of all optimal codes, not all maximizing codebooks up to equivalence. An equivalent theorem in unavailable or unindexed literature remains possible. No independent scientific audit has been performed.

## References

1. A. Kreindel, I. B. Essayag, A. L. Zabokritskiy, *Multiset Deletion Codes: Cyclic Constructions, Bounds, and Exact Results* (first public 9 January 2026), arXiv:2601.05636, https://arxiv.org/abs/2601.05636.
2. M. Kovačević and V. Y. F. Tan, *Codes in the Space of Multisets—Coding for Permutation Channels With Impairments* (first public December 2016), arXiv:1612.08837, https://arxiv.org/abs/1612.08837.
3. A. D. Lin, *Lower Bounds for all List-Decodable Deletion Codes* (September 2026), arXiv:2609.26650, https://arxiv.org/abs/2609.26650.
