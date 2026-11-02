# Every exchange-local PAV apportionment is globally optimal with at most three parties

## Finding

**Theorem (three-party local-to-global principle).** For every finite approval electorate, any number \(m\) of parties with \(1\le m\le3\), and any integer house size \(K\ge1\), every allocation of \(K\) seats that is a one-seat-exchange local maximum of proportional approval voting (PAV) is a global PAV maximum. The converse follows from the definition. For three parties, an exact global maximizer can be constructed by a greedy sequence of \(K\) marginal additions after computing ballot-type counts. The party-count bound cannot be increased to four, as shown by the previously published four-party counterexample in Gölz and Yaghoubizade, Example B.3 (2026); that counterexample is not claimed as new.

## Assumptions and scope

There are \(m\) labeled parties and finitely many voters, each approving any nonempty subset of parties. An apportionment is an integer vector \(\mathbf{k}=(k_1,\ldots,k_m)\) of nonnegative seats summing to \(K\). A voter's utility is the number of seats among approved parties. Define \(H_0=0\) and \(H_t=\sum_{h=1}^{t}1/h\) for positive integers \(t\). PAV scores each allocation by \(F(\mathbf{k})=\sum_v H_{\sum_{i\in A_v}k_i}\). A one-seat exchange removes a seat from a party with positive allocation and adds it to a different party. An exchange-local maximum is an allocation for which every such change weakly reduces \(F\). Ties are allowed. No bound on electorate size, house size, multiplicities, or approval overlap is assumed.

## Proof

When \(m=3\), let \(a_i\) count voters approving exactly party \(i\), let \(b_i\) count voters approving the other two parties but not party \(i\), and let \(c\) count voters approving all three. On the integer simplex \(k_1+k_2+k_3=K\), a ballot for the other two parties gives utility \(K-k_i\), while a ballot for all three gives constant utility \(K\). Thus

\[
F(\mathbf{k})=cH_K+\sum_{i=1}^{3}f_i(k_i),\qquad
f_i(t)=a_iH_t+b_iH_{K-t}\quad(0\le t\le K).
\]

For each \(0\le t<K\), its forward marginal is

\[
\Delta_i(t)=f_i(t+1)-f_i(t)=\frac{a_i}{t+1}-\frac{b_i}{K-t}.
\]

This quantity is nonincreasing in \(t\): its first term decreases and its second term also decreases. The allocation's variable score is the sum of its selected marginal increments \(\Delta_i(0),\ldots,\Delta_i(k_i-1)\), plus the constant \(\sum_i f_i(0)\). Under an exchange from \(i\) (with \(k_i>0\)) to \(j\ne i\), the score changes by \(\Delta_j(k_j)-\Delta_i(k_i-1)\). Therefore exchange-local maximality says that every last selected marginal is at least every first unselected marginal from a different party. By monotonicity, every earlier selected marginal is no smaller than the last selected in its own party, and every later unselected marginal is no larger than the first unselected in its own party. Hence each selected marginal is at least each unselected marginal, including those within the same party. The \(K\) selected marginals are therefore a choice of the \(K\) largest entries from all three marginal sequences, counting ties. Such a selection maximizes their sum among all feasible selections, proving global optimality. Equivalently, repeatedly selecting the party with the largest next marginal produces an optimum. The construction respects the prefix property because each marginal sequence is nonincreasing.

For \(m=2\), the PAV objective is an integer-concave function of the first party's seat count, since each ballot supports the first, second, or both; its first differences are nonincreasing. A point with no improving move to either neighbor is global. For \(m=1\), the feasible outcome is unique. Conversely every global optimum is exchange-local by definition.

The party-count boundary is sharp *as a classification*, but its negative side was already published. Gölz and Yaghoubizade (2026, Appendix B, Example B.3 and Proposition B.8) give \(K=2\), four parties \(a,b,c,d\), and four voters approving respectively \(\{a,c\}\), \(\{a,d\}\), \(\{b,c,d\}\), \(\{b\}\). The allocation \(\{c,d\}\) is exchange-local with PAV score \(7/2\), yet \(\{a,b\}\) scores \(4\). The new part of the theorem is the positive universal guarantee for at most three parties.

## Verification

Run `python3 verify.py` from the directory containing this document and the verifier. The exact-rational checker exhaustively tests every profile with zero-or-one voters per nonempty approval type, for one through three parties and house sizes one through six, checking \(10{,}852\) allocation instances; no exchange-local, nonglobal outcome occurs. The verifier independently checks the cited four-party, four-voter counterexample and its global maximum. These finite checks corroborate but do not replace the infinite proof.

## Relationship to prior work

Gölz and Yaghoubizade (2026) study PAV-optimality and local PAV-optimality in approval-based apportionment; their Theorem 2.3 proves local PAV implies priceability, while their Example B.3 already demonstrates that a local optimum need not be global with four parties and two seats. Therefore a four-party obstruction itself is not new, and it is not the claimed contribution here. The present theorem isolates the positive all-instance, all-house-size three-party boundary, which is not stated in the inspected relevant material of their paper. Brill et al. (2024) establish core and local-search guarantees for the wider model but do not give this local-to-global three-party classification. Standard separable discrete-concavity reasoning is the proof tool, not asserted to be a new general theorem.

## Limitations

The result is limited to at most three distinct parties; it does not imply that local PAV search is globally correct in general, and it does not establish a bound for arbitrary candidate-approval elections with individual committee candidates. The greedy procedure makes \(K\) iterations and should not be described as polynomial in the binary encoding length of an unbounded \(K\). No assertion of priority over unpublished or differently formulated three-party results is made. Independent scientific assessment has not been performed.

## References

1. P. Gölz and H. Yaghoubizade, *Approval-Based Apportionment: Like Portioning, Approximately like Committee Voting*, first publicly submitted 2026-08-27, arXiv:2608.27605, https://arxiv.org/abs/2608.27605 . See Theorem 2.3, Appendix B, Example B.3 and Proposition B.8; author-hosted full text https://paulgoelz.de/papers/model.pdf .
2. M. Brill, P. Gölz, D. Peters, U. Schmidt-Kraepelin, and K. Wilker, *Approval-Based Apportionment*, Mathematical Programming 203 (2024), 77–105, https://doi.org/10.1007/s10107-022-01852-1 , open-access version https://wrap.warwick.ac.uk/id/eprint/170677/1/s10107-022-01852-1.pdf .
