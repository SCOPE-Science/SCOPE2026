# All one-leak zero-forcing sets of complete prisms: a closed polynomial and minimal-set classification

## Finding

Let \(H_n=K_n\square K_2\), with \(n\ge3\), and let its two labeled clique layers be \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\); the only cross-layer edges are \(a_ib_i\). A set \(S\subseteq V(H_n)\) is **one-leaky forcing** if the usual blue-vertex/unique-white-neighbor color-change rule colors every vertex, regardless of which single vertex (possibly initially white) is declared unable to perform forces.

For \(n\ge4\), such a set has exactly one of the following types, allowing an overlap in the last two alternatives:

1. It contains one full clique layer.
2. It contains exactly \(n-1\) vertices of \(A\), missing \(a_i\), and contains at least two vertices of \(B\) whose indices differ from \(i\).
3. The corresponding symmetric condition with \(A\) and \(B\) interchanged.

The word **exactly** refers only to the nearly full layer; the other layer can have any size satisfying the condition. For \(n=3\), the complete characterization is: \(S\) contains an entire layer, or contains two vertices in *each* layer.

Write \(\mathcal L_n(z)=\sum_{S\text{ one-leaky forcing}}z^{|S|}\). For every \(n\ge4\),
\[
\boxed{\mathcal L_n(z)=2z^n(1+z)^n-z^{2n}+2n\binom{n-1}{2}z^{n+1}+2n\sum_{t=3}^{n-2}\binom nt z^{n-1+t}+n^2z^{2n-2}.}
\]
The sum is empty if its upper limit is below its lower limit. For \(n=3\),
\[
\boxed{\mathcal L_3(z)=2z^3+15z^4+6z^5+z^6.}
\]
The polynomial enumerating **inclusion-minimal** one-leaky forcing sets is
\[
\boxed{\mathcal I_n(z)=\begin{cases}2z^3+9z^4,&n=3,\\2z^n+2n\binom{n-1}{2}z^{n+1},&n\ge4.\end{cases}}
\]
In particular the one-leaky forcing number is \(Z_{(1)}(H_n)=n\); the only minimum one-leaky forcing sets are the two entire clique layers. For \(n\ge4\), the \(2n\binom{n-1}{2}\) nonminimum inclusion-minimal sets have size \(n+1\). For \(n=3\), there are nine nonminimum inclusion-minimal sets of size four.

## Assumptions and scope

All graphs are finite, simple, and undirected. A leak is any specified vertex prohibited from performing a force, but it may still be initially blue or become blue. We require success for **every** choice of one leak (equivalently, for at most one leak). Set cardinalities count *labeled* vertex subsets, not orbits of automorphisms. The parameter \(n\) ranges over every integer at least three; \(K_2\square K_2\) is not part of the claim.

## Proof

**Step 1: No start without a nearly full layer.** If \(S\) leaves at least two initially white vertices in each clique, every blue vertex has at least two white neighbors in its own clique. Thus no force is initially available even without a leak. Hence a one-leaky forcing set must contain an entire layer or all but one vertex of a layer.

**Step 2: A full layer always suffices.** Suppose \(A\subseteq S\). For a chosen leak \(v\), every initially white \(b_j\) can be forced by the already-blue \(a_j\), except possibly \(b_k\) when the leaked vertex is \(a_k\). Carry out those possible cross-layer forces first. If \(b_k\) is still white, all other \(b_j\) are blue. Since \(n\ge3\), a blue \(b_j\), \(j\ne k\), has \(b_k\) as its only white neighbor and is not the leak (the leak is \(a_k\)); it completes the forcing. If the leak lies in \(B\), all vertices of \(A\) can force normally. This proves sufficiency for both full-layer families.

**Step 3: One nearly full layer for \(n\ge4\).** Suppose \(A\cap S=A\setminus\{a_i\}\), while \(B\not\subseteq S\). Let \(T=\{j:b_j\in S\}\). Initially an \(a_j\), \(j\ne i\), can force \(a_i\) precisely when \(j\in T\): its only possibly white neighbors are \(a_i\) and \(b_j\). Since \(|T|\le n-1\), every blue vertex of \(B\) has at least one white neighbor inside \(B\). If \(|T|\le n-2\), it has at least two white same-layer neighbors and cannot force at the first step. If \(|T|=n-1\), there are at least \(n-2\ge2\) indices in \(T\setminus\{i\}\). Thus when \(|T\setminus\{i\}|\le1\), we necessarily have \(|T|\le n-2\), and a single leak on the unique initially available forcer \(a_j\) (if one exists) blocks every possible first force. This proves necessity of \(|T\setminus\{i\}|\ge2\).

Conversely, suppose \(|T\setminus\{i\}|\ge2\). At most one of the distinct vertices \(a_j\) for \(j\in T\setminus\{i\}\) is the leak, so another forces \(a_i\). Now the whole clique \(A\) is blue. Every white \(b_j\) can be forced from \(a_j\) unless the leak is that particular \(a_j\). With only one leak, all but at most one of the white vertices of \(B\) become blue. If a last white \(b_j\) remains, the leak must lie in \(A\); some blue \(b_k\) with \(k\ne j\) is not a leak and forces it within the clique \(B\). Such \(b_k\) exists since \(|T|\ge2\). This proves sufficiency. Interchange \(A\) and \(B\) for the symmetric case.

**Step 4: The exceptional triangular layers.** For \(n=3\), no set with at most one blue vertex in each layer can initiate a force. If \(A\) has two selected vertices but \(B\) at most one, then either no initial force is possible or the sole initial forcer \(a_j\) may be declared the leak. The same argument works with the layers reversed. If both layers have exactly two blue vertices, let \(a_i\) and \(b_j\) be their unique initially white vertices. When \(i=j\), at least two distinct blue vertices of \(A\) can force \(a_i\), and at least two distinct blue vertices of \(B\) can force \(b_i\); one leak cannot prevent completing the process. When \(i\ne j\), let \(k\) be the third index. The two distinct initial forcers \(a_k\) and \(b_k\) can force \(a_i\) and \(b_j\), respectively. At least one is not leaked; that force completes a full layer, and Step 2 (applied to the remaining leak) completes the other. Thus all nine configurations with two chosen vertices per layer qualify, proving the exceptional classification.

**Step 5: Count the configurations.** Full-layer sets contribute \(2z^n(1+z)^n-z^{2n}\) by inclusion-exclusion. For \(n\ge4\), configurations with exactly \(n-1\) vertices in one layer and exactly two in the other have \(n\binom{n-1}{2}\) choices per orientation, because both chosen opposite indices must avoid the missing index. If the other layer contains \(3\le t\le n-2\) vertices, any choice of those vertices contains two indices other than the missing one: there are \(n\binom nt\) per orientation. Finally, both layers can have exactly \(n-1\) chosen vertices in \(n^2\) ways. The last family is counted only once despite fitting both orientations. These disjoint contributions give \(\mathcal L_n\). For \(n=3\), full-layer contributions plus the nine two-plus-two sets give \(\mathcal L_3\).

**Step 6: Inclusion-minimality.** Any set strictly containing a complete clique layer is not inclusion-minimal, while each full layer itself is. For \(n\ge4\), a qualifying set without a full layer contains one of the sets with \(n-1\) vertices in one layer and exactly two opposite vertices whose indices avoid the omission; such a set is inclusion-minimal, since deleting an initially blue vertex from the nearly full layer leaves two white vertices there and at least two whites in the opposite layer, while deleting one of the two opposite vertices leaves only one eligible initial forcer and can be defeated by one leak. For \(n=3\), the nine two-plus-two sets are inclusion-minimal for the same classification reason. This gives \(\mathcal I_n\) and the minimum statements. \(\square\)

## Verification

The standalone `verify_leaky_prisms.py` constructs the two cliques and matching from their adjacency relation, computes a forcing closure separately for every possible single leaked vertex using the original color-change rule, and compares success with the theorem's case split. It exhausts every initial subset for each \(n\) from three through seven, compares the complete cardinality histograms against the displayed polynomial, and compares inclusion-minimal configurations against the stated classifications. This is finite corroboration and **not** a proof for arbitrary \(n\). The proof above supplies the infinite argument.

## Relationship to prior work

Alameda, Dillman and Kenter defined vertex-leaky forcing and developed fort and product bounds; their Cartesian-product upper bound addresses optimum size, not this complete-prism all-cardinality census. Alameda, Kritschgau, Warnberg and Young study general resilience criteria. Herrman and Wisdom analyze *categorical/direct* products \(K_n\times P_t\) and \(K_n\times C_t\), which differ from the Cartesian product \(K_n\square K_2\) here. Boyer et al. introduce the ordinary (zero-leak) forcing polynomial. Wang's 2026 general modular-compression framework gives an abstract enumeration mechanism for leaky sets but does not give this explicit complete-prism polynomial or the minimal-set classification; its generality should not be mistaken for a quoted specialized closed formula. The ordinary zero-forcing number of \(H_n\) is \(n\); its equality with \(Z_{(1)}(H_n)\) is therefore resilience rather than an increase in minimum sensor count. The assessed contribution is the **full one-leak set classification**, its closed coefficients, and irredundant spectrum, not the definition of leaky forcing or a generic existence algorithm.

## Limitations

Only one unavailable forcer is permitted, and no claims are made for two or more simultaneous leaks, positive-semidefinite forcing, or products with more than two clique layers. Full literature priority cannot be guaranteed, particularly for alternative network-reliability terminology; a broader general-purpose enumeration algorithm also does not establish that this closed specialization has not appeared elsewhere.

## References

1. S. Dillman and F. Kenter, *Leaky Forcing: A New Variation of Zero Forcing*, arXiv:1910.00168, first posted 2019-10-01, https://arxiv.org/abs/1910.00168. Later journal version: J. S. Alameda, S. Dillman, F. Kenter, *Leaky forcing: a new variation of zero forcing*, Australasian Journal of Combinatorics 88 (2024), 308–326, https://ajc.maths.uq.edu.au/pdf/88/ajc_v88_p308.pdf.
2. J. S. Alameda, J. Kritschgau, N. Warnberg, M. Young, *On leaky forcing and resilience*, arXiv:2008.06552 (2020), https://arxiv.org/abs/2008.06552.
3. K. Boyer et al., *The zero forcing polynomial of a graph*, arXiv:1801.08910, first posted 2018-01-26, https://arxiv.org/abs/1801.08910.
4. R. Herrman and G. Wisdom, *Leaky forcing and resilience of Cartesian products of \(K_n\)* [the main results concern direct/categorical products], arXiv:2411.03178 (2024), https://arxiv.org/html/2411.03178v1.
5. X. Wang, *Modular Compression of Leaky Forts and Leaky Forcing Polynomials*, public preprint (2026), doi:10.5281/zenodo.20388397, https://www.researchgate.net/publication/405317381_Modular_Compression_of_Leaky_Forts_and_Leaky_Forcing_Polynomials.
