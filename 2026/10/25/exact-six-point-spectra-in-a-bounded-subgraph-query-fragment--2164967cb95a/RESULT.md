# Exact six-point spectra in a bounded subgraph-query fragment

## Finding

Let \(\mathcal B_4^{\mathrm{sub}}\) be the Boolean closure (under finite conjunction, disjunction, and negation) of the graph properties \(\mathrm{Sub}_H\), where \(H\) ranges over finite simple graphs with at most four vertices and \(\mathrm{Sub}_H(G)\) means that \(G\) contains a not-necessarily-induced copy of \(H\). For \(\varphi\in\mathcal B_4^{\mathrm{sub}}\), define

\[
\operatorname{Spec}(\varphi)=\{\alpha>0:\Pr[G(n,n^{-\alpha})\models\varphi]\text{ does not tend to }0\text{ or }1\}.
\]

The exact maximum of \(|\operatorname{Spec}(\varphi)|\) over this fragment is six. Every such spectrum is contained in

\[
S=\left\{\frac23,\frac45,1,\frac43,\frac32,2\right\},
\]

and the bound is attained by the parity sentence

\[
\varphi_* = \mathrm{Sub}_{K_4}\oplus\mathrm{Sub}_{K_4-e}\oplus\mathrm{Sub}_{K_3}\oplus\mathrm{Sub}_{P_4}\oplus\mathrm{Sub}_{P_3}\oplus\mathrm{Sub}_{K_2},
\]

where \(\oplus\) is Boolean exclusive-or. Its limiting truth probabilities at the six exponents, in increasing order, are

\[
\left(e^{-1/24},\ 1-e^{-1/4},\ e^{-1/6},\ 1-e^{-1/2},\ e^{-1/2},\ 1-e^{-1/2}\right).
\]

## Assumptions and scope

The random graph \(G(n,p)\) is the simple undirected binomial random graph on \([n]\), with each edge present independently with probability \(p\). The spectrum uses the exact power law \(p=n^{-\alpha}\), with fixed \(\alpha>0\). The fragment is specifically the Boolean closure of non-induced subgraph-occurrence properties for patterns on at most four vertices; this is a proper subfragment of all first-order sentences of quantifier depth at most four. Graph names \(K_4\), \(K_4-e\), \(K_3\), \(P_4\), \(P_3\), and \(K_2\) have their usual meanings.

## Proof

**Upper bound.** For a fixed graph \(H\), let

\[
\rho_{\max}(H)=\max_{J\subseteq H,\,v(J)>0}\frac{e(J)}{v(J)}
\]

be its maximum subgraph density, ignoring zero-edge subgraphs when taking a positive maximum. The standard subgraph-threshold theorem gives threshold order \(n^{-1/\rho_{\max}(H)}\) for the event \(\mathrm{Sub}_H\). Hence, at \(p=n^{-\alpha}\), this event tends to probability one when \(\alpha<1/\rho_{\max}(H)\), and to probability zero when \(\alpha>1/\rho_{\max}(H)\).

A complete enumeration of simple graphs on at most four vertices gives the possible positive maximum densities

\[
\rho_{\max}(H)\in\left\{\frac12,\frac23,\frac34,1,\frac54,\frac32\right\}.
\]

Their reciprocals are exactly the six elements of \(S\). Every generator \(\mathrm{Sub}_H\) of \(\mathcal B_4^{\mathrm{sub}}\) therefore has a deterministic zero-one limit outside \(S\). A finite Boolean combination of events with deterministic zero-one limits also has a deterministic zero-one limit, proving \(\operatorname{Spec}(\varphi)\subseteq S\) for every \(\varphi\) in the fragment.

**Sharpness.** The six representative graphs in \(\varphi_*\) are strictly balanced: every proper subgraph has smaller edge-to-vertex ratio. For a strictly balanced fixed graph \(H\) at \(p=n^{-v(H)/e(H)}\), the number of copies converges to a Poisson random variable of mean \(1/|\operatorname{Aut}(H)|\). The required data are:

| Pattern \(H\) | \(v(H)\) | \(e(H)\) | Critical \(\alpha=v(H)/e(H)\) | \(|\operatorname{Aut}(H)|\) | Poisson mean |
|---|---:|---:|---:|---:|---:|
| \(K_4\) | 4 | 6 | \(2/3\) | 24 | \(1/24\) |
| \(K_4-e\) | 4 | 5 | \(4/5\) | 4 | \(1/4\) |
| \(K_3\) | 3 | 3 | \(1\) | 6 | \(1/6\) |
| \(P_4\) | 4 | 3 | \(4/3\) | 2 | \(1/2\) |
| \(P_3\) | 3 | 2 | \(3/2\) | 2 | \(1/2\) |
| \(K_2\) | 2 | 1 | \(2\) | 2 | \(1/2\) |

At each critical exponent exactly one of the six occurrence indicators has a non-degenerate Poisson limit; the other five tend to zero or one. The parity of those five deterministic indicators makes \(\varphi_*\) reduce to the target occurrence event or its complement as follows:

| Critical \(\alpha\) | Reduced event for \(\varphi_*\) | Limit of \(\Pr[G(n,n^{-\alpha})\models\varphi_*]\) |
|---:|---|---:|
| \(2/3\) | no \(K_4\) | \(e^{-1/24}\) |
| \(4/5\) | contains \(K_4-e\) | \(1-e^{-1/4}\) |
| \(1\) | no \(K_3\) | \(e^{-1/6}\) |
| \(4/3\) | contains \(P_4\) | \(1-e^{-1/2}\) |
| \(3/2\) | no \(P_3\) | \(e^{-1/2}\) |
| \(2\) | contains \(K_2\) | \(1-e^{-1/2}\) |

Every displayed limit lies strictly between zero and one, so all six exponents belong to \(\operatorname{Spec}(\varphi_*)\). The upper bound then proves \(\operatorname{Spec}(\varphi_*)=S\) and the exact maximum cardinality is six.

## Verification

The included standalone script `support/verify_spectrum_fragment.py` enumerates all labeled simple graphs on one through four vertices, checks the complete set of positive maximum subgraph densities, and verifies the six representative automorphism-group sizes and reciprocal exponents. It reports `VERIFICATION_OK`. This finite check supports the finite classification and constants; it is not used as a substitute for the asymptotic threshold or Poisson-limit arguments, which are supplied analytically above and in the cited random-graph literature.

## Relationship to prior work

Yarovikov and Zhukovskii prove that the spectrum of the full first-order quantifier-depth-four fragment is finite and recall the threshold theorem for fixed subgraph occurrence [1, 2]. Those results give the general context and the threshold mechanism, but do not state the exact maximum cardinality for the Boolean subgraph-occurrence fragment defined here. The classical strictly balanced graph literature supplies the Poisson limit used for the witness [3, 4]. The present claim is restricted to the exact six-point maximum and explicit witness in \(\mathcal B_4^{\mathrm{sub}}\); it does not assert that six is the maximum for all first-order sentences of quantifier depth four.

## Limitations

The result classifies a natural bounded-pattern fragment, not the full first-order quantifier-depth-four spectrum. It uses standard subgraph-threshold and strictly balanced Poisson theorems; the finite script checks only the density list and finite automorphism counts. Targeted literature and database searches did not locate this exact fragment-specific maximum, but failed searches cannot establish absolute historical priority. The full texts of the cited 1986 threshold paper and 1990 Poisson-limit paper were not directly inspected; their relevant role is also supported by the inspected 2021 primary text and the explicit proof above.

## References

[1] Y. Yarovikov and M. Zhukovskii, “Spectrum of FO logic with quantifier depth 4 is finite,” arXiv:2111.11470v1, first public 2021-11-22. https://arxiv.org/abs/2111.11470

[2] Y. Yarovikov and M. Zhukovskii, “Spectrum of FO Logic with Quantifier Depth 4 is Finite,” *ACM Transactions on Computational Logic* 25(2), Article 9 (2024). DOI: 10.1145/3641547.

[3] A. Ruciński and A. Vince, “Strongly balanced graphs and random graphs,” *Journal of Graph Theory* 10(2) (1986), 251–264. DOI: 10.1002/jgt.3190100214.

[4] W. C. S. Suen, “A correlation inequality and a Poisson limit theorem for nonoverlapping balanced subgraphs of a random graph,” *Random Structures & Algorithms* 1 (1990), 231–242. DOI: 10.1002/rsa.3240010210.
