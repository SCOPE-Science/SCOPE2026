# Prime-field simplex tight sampling has a unique ternary optimizer orbit

## Finding
Let \(p\) be any prime, let \(G_p=\mathbb F_p^3\), and fix the affine-independent four-point set
\[
A_p=\{0,e_1,e_2,e_3\}\subset G_p.
\]
Identify the dual group with \(G_p\) by \(\chi_b(a)=\exp(2\pi i\,a\cdot b/p)\). For a **set of distinct frequencies** \(B\subset G_p\), form the \(4\times |B|\) Fourier sampling matrix
\[
M_B=(\chi_b(a))_{a\in A_p,\ b\in B}.
\]
Call \(B\) tight when \(M_BM_B^*=|B|I_4\); equivalently, its four-dimensional restricted character vectors form a tight frame with bound \(|B|\) in the unnormalized convention. Define the minimum cardinality \(r_p\) among nonempty tight frequency sets.

**Prime-field cutoff theorem.** The exact minimum is
\[
r_p=\begin{cases}
4,&p=2,\\
6,&p=3,\\
p,&p\ge5.
\end{cases}
\]
At \(p=2\), precisely two four-frequency sets are optimal: the even- and odd-parity affine planes in \(\mathbb F_2^3\).

At \(p=3\), precisely **27** distinct six-frequency sets are optimal, and they form **one translation orbit**. A representative is
\[
B_0=\{(0,0,0),(0,1,1),(1,0,2),(1,2,0),(2,1,2),(2,2,1)\}.
\]
Every optimum is \(B_0+t\) for a unique \(t\in\mathbb F_3^3\). For every prime \(p\ge5\), the line
\[
B_p=\{t(1,2,3):t\in\mathbb F_p\}
\]
is a minimum-size tight frequency set. The classification of all minimum-size sets for \(p\ge5\) is not asserted.

## Assumptions and scope
All sets are genuine subsets of the character group: repeated frequencies and arbitrary weights are excluded. The Fourier vectors are \((\chi_b(a))_{a\in A_p}\) with counting-measure inner product on \(A_p\). Since every vector has squared norm \(4\), dividing columns by \(2\) gives a unit-vector tight frame with bound \(|B|/4\). This normalization does not change which sets are tight.

The underlying objects are *subsets of character frequencies producing a tight restricted frame*, not complete group orbits or Riesz bases. The four sample points constitute the smallest affinely independent simplex in rank three. For odd \(p\), a sum of four \(p\)-th roots of unity cannot vanish because \(p\nmid4\). Thus no two distinct character restrictions to \(A_p\) can be orthogonal, and \(A_p\) is not spectral. Extra distinct frequencies provide a natural exact-tightness substitute for an orthogonal exponential basis.

## Proof
### Necessary cardinality
For distinct \(a,a'\in A_p\), the off-diagonal Gram entry is
\[
(M_BM_B^*)_{a,a'}=\sum_{b\in B}\exp\!\left(2\pi i\,(a-a')\cdot b/p\right).
\]
Up to sign the six nonzero differences are
\[
D_p=\{e_1,e_2,e_3,e_1-e_2,e_1-e_3,e_2-e_3\}.
\]
For any \(d\in D_p\), let \(c_j\) count frequencies satisfying \(d\cdot b=j\) in \(\mathbb F_p\). The vanishing Gram entry is \(\sum_{j=0}^{p-1}c_j\omega^j=0\), with \(\omega=\exp(2\pi i/p)\). Because \(p\) is prime, the minimal polynomial of \(\omega\) over \(\mathbb Q\) is \(1+z+\cdots+z^{p-1}\). Hence
\[
c_0=c_1=\cdots=c_{p-1}=|B|/p,
\]
and \(p\) divides \(|B|\). The rank-four identity \(M_BM_B^*=|B|I_4\) also requires \(|B|\ge4\). Thus \(|B|\) is at least the smallest multiple of \(p\) not below four.

### Constructions at every prime
For \(p=2\), take the even-parity plane
\[
B_2=\{000,011,101,110\},
\]
where each three-digit word denotes an element of \(\mathbb F_2^3\). Each of the six directions in \(D_2\) has two zeros and two ones on this plane, so \(M_{B_2}M_{B_2}^*=4I_4\).

The binary optimizer classification also follows without computation. The six distinct directions in \(D_2\) are all nonzero characters except \(u=(1,1,1)\). If \(|B|=4\) is tight, the Fourier coefficients of \(\mathbf1_B\) vanish away from the trivial character and \(u\). Fourier inversion then gives
\[
\mathbf1_B(x)=\tfrac12+c(-1)^{x_1+x_2+x_3}.
\]
Because \(\mathbf1_B\) only takes the values zero and one, \(c=\pm\tfrac12\). Hence \(B\) is one of the two parity planes.

For every prime \(p\ge5\), put \(v=(1,2,3)\) and \(B_p=\{tv:t\in\mathbb F_p\}\). For each \(d\in D_p\),
\[
d\cdot v\in\{1,2,3,-1,-2,-1\},
\]
all of whose members are nonzero modulo any prime \(p\ge5\). Consequently \(t\mapsto d\cdot (tv)\) runs through every field element exactly once. Its character sum vanishes; therefore \(M_{B_p}M_{B_p}^*=pI_4\). This attains the necessary bound.

For \(p=3\), the six points \(B_0\) displayed above have the following exact property: for each of the six directions in \(D_3\), each residue \(0,1,2\) occurs **twice** among \(d\cdot b\), \(b\in B_0\). Thus \(M_{B_0}M_{B_0}^*=6I_4\), attaining the lower bound.

### Exhaustive ternary rigidity
Tightness of a six-point set is *equivalent* to the six exact, finite conditions
\[
\#\{b\in B:d\cdot b=j\}=2
\quad(d\in D_3,\ j=0,1,2).
\]
Every six-point \(B\) has a translate containing zero, so it suffices to test the \(\binom{26}{5}=65{,}780\) subsets obtained by adjoining zero to five distinct nonzero vectors. Exhaustive integer testing, reproduced in `verify_tetrahedron.py`, returns exactly these six normalized sets (each row lists all six ternary coordinate triples):

| | All frequencies in the normalized set |
|---|---|
| 1 | `000 011 102 120 212 221` |
| 2 | `000 012 101 122 210 221` |
| 3 | `000 012 102 121 211 220` |
| 4 | `000 021 110 122 201 212` |
| 5 | `000 021 112 120 202 211` |
| 6 | `000 022 112 121 201 210` |

These six sets are, by direct coordinate comparison, exactly \(B_0-b\) for the six \(b\in B_0\). Therefore every minimizing \(B\) is a translate of \(B_0\). No nonzero translation stabilizes \(B_0\): a stabilizing vector would generate a three-point affine line wholly contained in \(B_0\), but checking the \(\binom63=20\) triples shows that no three elements of \(B_0\) are collinear (equivalently, no three sum to zero in \(\mathbb F_3^3\)). Thus the translation orbit has exactly \(27\) members.

For an independent finite-count verification, the same standalone program also examines every one of the \(\binom{27}{6}=296{,}010\) unrestricted six-point frequency sets, checks the six balanced projections with exact integers, and confirms that the complete answer is precisely those \(27\) translates. The enumeration is genuinely exhaustive because its iterators run through every combination of the finite group elements; there is no numerical tolerance, pruning heuristic, timeout assumption, or inference about infinite domains from the finite computation.

## Verification
From the directory containing the complete supplied files, run:

```text
python3 verify_tetrahedron.py
```

The exact checker prints:

```text
p=2: tested 70 four-frequency sets; optimizers: 2
p=3: tested 296010 six-frequency sets; optimizers: 27
p=3 normalized: tested 65780 six-frequency sets through zero; optimizers: 6
p>=5: integer witness checks p=5,7,11,13 passed; general proof is symbolic.
```

For the ternary case the checker also computes the full \(4\times4\) Gram matrix in the basis \(1,\omega\), verifies all off-diagonal exponents occur with multiplicities \((2,2,2)\), and checks that translating \(B_0\) produces each and only each solution. The arbitrary-prime cutoff and line construction are proved algebraically above, not inferred from tested primes.

## Relationship to prior work
Marshall--Waldron study harmonic tight frames obtained by selecting character rows and retaining the **entire** underlying group orbit of columns. They count resulting frames up to unitary equivalence. Here the four sample rows are fixed and only a **proper subset of frequency columns** may be retained; the invariant is the exact smallest such subset and its distinct, unquotiented minimizing frequency sets. Neither the full-orbit construction nor its unitary-equivalence count determines the \(27\)-subset classification.

Ferguson--Mayeli--Sothanaphan study finite exponential **Riesz bases**, whose frequency and sample sets have equal cardinality, and quantitative conditioning. The odd-prime four-point simplex has no orthogonal exponential basis, and the present problem measures exactly how many *additional distinct characters* restore perfect tightness. Their basis-pair results therefore do not imply the overcomplete optimum.

Banica studies partial Butson matrices, giving exact descriptions at two and three rows for prime roots of unity and asymptotic counts. Those results explain the root-sum congruence but do not classify the present Fourier-structured four-row, six-column subsets.

The classical six-by-six ternary Butson--Hadamard or Tao matrix is a close structural relative. Huang--Liang--Chen discuss its uniqueness up to monomial equivalence among six-by-six cubic-root Hadamard matrices. That square-matrix statement does not specify which **six distinct group characters** give the present *four-by-six* Fourier restriction, nor imply a count of \(27\) translation-labelled subsets without further argument. Such compatibility with the fixed sample coordinates is essential in this finding.

## Limitations
The minimizer geometry for primes \(p\ge5\) is not classified beyond the explicit line construction. The exact ternary count is for frequency **sets**, not weighted multisets, equivalence classes under arbitrary coordinate changes, or full six-by-six Hadamard matrices.

The ternary rigidity is established by a small complete integer enumeration, not a closed-form uniform classification of higher-dimensional affine simplices. The prime-uniform cardinality formula has a separate symbolic proof. An unindexed result giving the same labelled Fourier-subset classification may exist; no independence or external certification is claimed.

## References
1. S. Marshall and S. Waldron, *On the number of harmonic frames*, arXiv:1611.07121v1, 22 November 2016; *Applied and Computational Harmonic Analysis* 48 (2020), 46--63, DOI 10.1016/j.acha.2018.02.004.
2. S. Ferguson, A. Mayeli and N. Sothanaphan, *Riesz bases of exponentials and multi-tiling in finite abelian groups*, arXiv:1904.04487v1, 9 April 2019.
3. T. Banica, *Counting results for thin Butson matrices*, *Electronic Journal of Combinatorics* 21(3) (2014), P3.12, DOI 10.37236/3891.
4. Y. Huang, M. Liang and L. Chen, *Order-six CHMs containing exactly three distinct elements*, arXiv:2412.01334v1, 2 December 2024.
