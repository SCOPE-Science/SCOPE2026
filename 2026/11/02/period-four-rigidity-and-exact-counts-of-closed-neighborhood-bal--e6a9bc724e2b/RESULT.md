# Period-four rigidity and exact counts of closed-neighborhood balanced colorings on clique cylinders

## Finding
For every even integer \(m\ge4\) and every integer \(n\ge3\), let \(G_{m,n}=K_m\square C_n\), with labelled vertices \((a,j)\), \(a\in\{1,\ldots,m\}\), \(j\in\mathbb Z/n\mathbb Z\). A locally balanced two-coloring with closed neighborhoods is a function \(f:V(G_{m,n})\to\{0,1\}\) for which each vertex has exactly \((m+2)/2\) vertices of each color in its closed neighborhood. Denote the number of such functions, with the two color names and all vertices distinguished, by \(B(m,n)\).

**Theorem.** The complete enumeration is
\[
B(m,n)=\begin{cases}
\binom{m}{m/2}^{\!2},& 4\mid n,\\
0,& 4\nmid n.
\end{cases}
\]
All colorings consist of two arbitrarily chosen balanced sign columns \(u,v\in\{\pm1\}^{m}\), each containing exactly \(m/2\) positive entries, followed cyclically by \(-u,-v\). Each coloring uses both colors, hence the number of partitions up to exchanging color names is \(B(m,n)/2\).

## Assumptions and scope
All graphs are finite, undirected, loopless, and simple; the cycle \(C_n\) has length \(n\ge3\), and \(K_m\) is the clique of order \(m\). The Cartesian product joins \((a,j)\) to \((b,k)\) exactly when either \(j=k\) and \(a\ne b\), or \(a=b\) and \(k-j\equiv\pm1\pmod n\). Each closed neighborhood is the complete \(m\)-vertex column together with the two vertices at adjacent cycle coordinates in the same row. Its cardinality is \(m+2\). Because \(m\) is even, locally balanced in the usual at-most-one discrepancy sense is equivalent to exact equality. Two color names are fixed, so global color interchange produces a distinct counted function.

## Proof
Write \(x_{a,j}=1\) for one color and \(x_{a,j}=-1\) for the other. Put \(S_j=\sum_{a=1}^{m}x_{a,j}\). The closed-neighborhood balance equations are, for every \(a,j\),
\[
S_j+x_{a,j-1}+x_{a,j+1}=0.\tag{1}
\]
Summing (1) over the row coordinate yields the scalar cyclic recurrence
\[
S_{j-1}+mS_j+S_{j+1}=0.\tag{2}
\]

Set \(M=\max_j|S_j|\). Choose a coordinate attaining \(M\). Equation (2) implies \(mM\le |S_{j-1}|+|S_{j+1}|\le2M\); since \(m>2\), necessarily \(M=0\). Thus every column contains exactly half of each color. Equation (1) reduces to \(x_{a,j+1}=-x_{a,j-1}\), or \(x_{a,j+2}=-x_{a,j}\). Each row has period four and lacks periods one and two, since a sign is never its own negative. Thus four is the least period and \(4\mid n\) is necessary. When \(4\mid n\), choose independently any two sign columns \(u,v\) with \(m/2\) positive coordinates and repeat \(u,v,-u,-v\) around the cylinder. These and only these solve (1). Distinct choices of \(u,v\) yield distinct labelled colorings, giving \(\binom{m}{m/2}^{2}\). \(\square\)

## Comparison: the thin prism
The count for \(m=2\) can be read from the cyclic-prism parity kernel [5]. Write the upper and lower binary layers as \(a_j,b_j\). Parity forces \(a_{j+4}=a_j\) and \(b_j=a_{j-1}+a_j+a_{j+1}\) over \(\mathbb F_2\). To have exact balance, no upper triple can be monochromatic: parity makes its fourth bit the same if all three coincide, and gives exactly two ones otherwise. For odd \(n\) the upper layer is constant; for \(n\equiv2\pmod4\) it must alternate, giving two patterns with \(b_j=a_j\). For \(4\mid n\), all upper triples are mixed exactly when a block of four has two ones. Then \(b_j=a_{j+2}\), so all lower triples are mixed too. This gives six patterns. This prism case is not part of the theorem's originality claim.

## Verification
The accompanying `verify_balance.py` tests actual closed neighborhoods of every assignment for ten small graphs, including \((m,n)=(4,4)\), where the count is \(36\). It also generates all candidate cyclic solutions from the first two columns for \(m\in\{2,4,6,8\}\), \(3\le n\le12\). Both tests include the thin prism as a comparison case outside the theorem's scope. Running the verifier prints `VERIFY_OK`. The finite checks do not replace the proof.

## Relationship to prior work
The closed-neighborhood locally balanced two-partition concept and hardness of deciding existence on several graph classes are studied by Gharibyan and Petrosyan, *Complexity results on locally-balanced 2-partitions of graphs*, original arXiv submission on 2024-01-27. Their statement is about general decision complexity, not exact counts for \(K_m\square C_n\). Gharibyan's 2020 paper determines existence of closed-neighborhood two-partitions on the rook graphs \(K_m\square K_n\), and studies different open-neighborhood questions on cycle powers; that rook-graph existence theorem does not imply the present counts for a clique–cycle product. The 2021 locally balanced \(k\)-partition paper and related 2021 dissertation abstract address other graph families, with a torus statement for open neighborhoods, not this closed-neighborhood enumeration. The 2018 grid-like graph work is a plausible priority source; available descriptions concern open-neighborhood grid/toroidal constructions, while its complete original text was not inspected. No claim of comprehensive publication priority is made. Equitable two-colorings with closed neighborhoods can also be viewed as balanced colorings of the closed-neighborhood incidence hypergraph; exact enumeration is the contribution here.

## Limitations
The theorem covers even clique orders \(m\ge4\) and simple cycles \(n\ge3\). Odd clique orders have odd closed-neighborhood sizes, so the at-most-one imbalance definition produces different inequalities not treated here. Open-neighborhood balance and non-Cartesian products are not addressed. The proof does not imply a new complexity bound. Literature coverage is not exhaustive, notably for the 2018 grid-like conference source and unindexed equivalent work.

## References
1. A. H. Gharibyan and P. A. Petrosyan, *Complexity results on locally-balanced 2-partitions of graphs*, arXiv:2401.15490v1, initial posting 2024-01-27, https://arxiv.org/abs/2401.15490.
2. A. H. Gharibyan, *On locally-balanced 2-partitions of some classes of graphs*, Proceedings of Yerevan State University, Physical and Mathematical Sciences 54(1) (2020), 9–19, https://doi.org/10.46991/PYSU:A/2020.54.1.009.
3. A. H. Gharibyan and P. A. Petrosyan, *Locally-balanced k-partitions of graphs*, Proceedings of Yerevan State University, Physical and Mathematical Sciences 55(2) (2021), https://doi.org/10.46991/PYSU:A/2021.55.2.096.
4. A. H. Gharibyan, *Investigation of locally-balanced partitions of graphs*, dissertation abstract (2021), https://degrees.hesc.am/sites/default/files/2021-06/PhD_abstract.pdf.
5. *Parity-kernel codes of cyclic prisms and their Reed–Muller support hierarchy*, Resultary record dated 2026-11-02, https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-parity-kernel-codes-of-cyclic-prisms-and-their-reed-muller-suppo--6f178222ad14/RESULT.md, Proof, equations (1)–(2).
