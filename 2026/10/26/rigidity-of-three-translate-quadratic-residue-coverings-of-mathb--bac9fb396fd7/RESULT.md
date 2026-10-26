# Rigidity of three-translate quadratic-residue coverings of \(\mathbb F_{25}\)

## Finding
Let \(F=\mathbb F_5[u]/(u^2-2)\), and let \(Q=\{x^2:x\in F\}\), including zero. There are exactly **100** unordered three-element subsets \(A\subset F\) such that \(A+Q=F\). Every one is a translate and nonzero-square multiple of
\[
A_0=\{0,u,1+3u\}.
\]
Equivalently, the complete family is
\[
A=\{a,a+t,a+t\lambda\},\quad a\in F,\quad \chi(t)=-1,\quad
\lambda^2-\lambda+1=0,
\]
with \(\chi\) the quadratic character of \(F\), and with repetitions from relabeling disregarded. All such sets are independent dominating triples in the Paley graph on \(25\) vertices. The minimum possible shift-set size is three. Under the affine-square group \(z\mapsto sz+a\) with \(s\in(F^\times)^2\), the family is one orbit of size \(100\), and each set has stabilizer of size \(3\).

## Assumptions and scope
The field is specifically \(F=\mathbb F_5[u]/(u^2-2)\); the polynomial is irreducible because \(2\) is not a square modulo \(5\). The symbol \(Q\) contains zero, so membership \(x\in A+Q\) is equivalent to \(x-a\) being zero or a nonzero square for at least one \(a\in A\). Every count is for **unordered** subsets of three distinct field elements. The result makes no assertion about the numbers of minimum coverings in other finite fields.

In the reproducibility encoding \(a+bu\leftrightarrow a+5b\), the two roots of \(\lambda^2-\lambda+1\) are \(13=3+2u\) and \(18=3+3u\); the witness above corresponds to \(\{0,5,16\}\).

## Proof
**1. Character-sum equality condition.** Extend the quadratic character by \(\chi(0)=0\). For distinct \(a,b,c\), let \(M\) be the number of points \(x\in F\) for which all three values \(\chi(x-a),\chi(x-b),\chi(x-c)\) equal \(-1\). Thus \(\{a,b,c\}+Q=F\) exactly when \(M=0\). Put
\[
T=\sum_{x\in F}\chi((x-a)(x-b)(x-c)),
\]
and let \(R\) be the number of members \(z\in\{a,b,c\}\) for which the two differences \(z-w\), with \(w\ne z\), are nonsquares. Since \(\chi(-1)=1\), one has \(0\le R\le3\), and \(R=3\) if and only if all three pairwise differences are nonsquares.

Expand \(\prod_{z\in\{a,b,c\}}(1-\chi(x-z))\) and sum over \(F\). The three linear sums vanish and each quadratic-character pair sum equals \(-1\), yielding \(25-3-T=22-T\). Away from the three roots, the product is \(8\) precisely at the \(M\) uncovered points and zero otherwise; a root contributes \(4\) precisely when counted by \(R\). Therefore
\[
22-T=8M+4R.\tag{1}
\]
The Hasse bound for the nonsingular curve \(y^2=(x-a)(x-b)(x-c)\) gives \(|T|\le10\). If \(M=0\), identity (1) gives \(T=22-4R\ge10\); hence **necessarily** \(R=3\) and \(T=10\). Conversely these equalities imply \(M=0\).

**2. Complete cubic-sum classification.** Every ordered triple of distinct points has a unique representation \((a,a+t,a+t\lambda)\), where \(t\in F^\times\) and \(\lambda\in F\setminus\{0,1\}\). Write
\[
T_\lambda=\sum_{x\in F}\chi(x(x-1)(x-\lambda)).
\]
After \(x=a+ty\), the cubic-sum scaling law is \(T=\chi(t)T_\lambda\). The equality \(R=3\) forces \(t\) to be a nonsquare, so that \(T=10\) requires \(T_\lambda=-10\).

Here is a complete exact calculation of \(T_\lambda\). Encode \(i=a+5b\) as \(a+bu\) with \(0\le a,b<5\). The set of squares, including zero, is
\[
Q=\{0,1,2,3,4,6,9,12,13,17,18,21,24\}.
\]
For the \(23\) admissible encoded parameters, direct addition and multiplication modulo \(u^2=2\), followed by the displayed \(25\)-term sum, give the **complete** table:

| \(T_\lambda\) | encoded values of \(\lambda\) |
| ---: | :--- |
| \(-10\) | \(13,18\) |
| \(-6\) | \(8,23\) |
| \(-2\) | \(5,6,7,9,20,21,22,24\) |
| \(2\) | \(10,11,15,16\) |
| \(6\) | \(2,3,4,12,14,17,19\) |

The first row consists exactly of the two roots of \(\lambda^2-\lambda+1=0\); both \(\lambda\) and \(\lambda-1\) are squares for either root. Consequently \(R=3\) and \(T=10\) hold if and only if \(t\) is a nonsquare and \(\lambda\) is one of these roots. This proves the asserted complete parametrization, without extrapolating from any partial search.

**3. Count and orbit.** There are \(25\) choices of \(a\), \(12\) nonsquare choices of \(t\), and two choices of \(\lambda\). Each unordered three-element set is represented exactly \(3!=6\) times, since all six orderings still have nonsquare pairwise differences. Thus the number is \(25\cdot12\cdot2/6=100\).

Let \(\lambda_0=18=3+3u\), so \(u\lambda_0=1+3u\). Every nonsquare \(t\) is \(su\) with \(s\) a nonzero square, hence the triples with \(\lambda=\lambda_0\) are affine-square images of \(A_0\). If instead \(\lambda=13\), swap the second and third points: the new ratio is \(1/\lambda=18\), and the new difference remains a nonsquare. Therefore every covering triple lies in the same affine-square orbit. That group has \(25\cdot12=300\) elements, so the stabilizer of any triple has order \(300/100=3\).

**4. Minimum cardinality.** Directly from the displayed square set, two distinct translates of \(Q\) intersect in \(7\) elements if the shift difference is a square and \(6\) if it is a nonsquare. Their union therefore has \(19\) or \(20\) elements, never \(25\). A single translate also cannot cover. The exhibited triple covers, so the minimum cardinality is three.

## Verification
The standalone `verifier.py` uses only Python's standard library and exact finite-field arithmetic. It computes all \(23\) cubic sums in the table, enumerates all \(\binom{25}{3}=2300\) unordered triples directly, checks that precisely \(100\) cover, and independently compares the resulting family both with the two-root parametrization and with the affine-square orbit of \(A_0\). It also tests identity (1) and the Hasse boundary for every triple, checks that no pair covers, and checks the stabilizer order. Execute `python3 verifier.py` from the extracted package directory. The finite enumeration covers the entire specified field, not a sample. The Hasse inequality is a standard theorem used only for the structural reduction; the direct checker independently verifies the exact finite classification.

## Relationship to prior work
Zhou and Wu's *Covering finite fields by translates of multiplicative subgroups* (arXiv:2610.25228v1, first submitted 18 October 2026) introduces the general minimum shift-number \(\tau(q,d)\), gives bounds and describes other special constructions; its inspected statements do not give a classification or count of quadratic-residue triple coverings of \(F\). In the equivalent language of domination in Paley graphs, Brouwer's published graph table already records that the domination number of the order-\(25\) Paley graph is \(3\). Brouwer and Martin, *Triple intersection numbers for the Paley graphs* (arXiv:2109.03654v1), prove that for odd \(q>25\) every three vertices have a common neighbor, and provide sharp character-sum bounds and a small-field range table; the character-sum strategy and threshold are therefore **not** claimed as new. The additional assertion here is the complete **100-member, single-orbit classification** at the extremal field size, not a rediscovery of the domination number or of the Hasse bound.

## Limitations
This is an exact finite-field classification for \(q=25\), not an asymptotic result or a classification for general \(q\). The uniqueness of the orbit is under the affine-square automorphism subgroup; the statement does not require classifying all graph automorphisms. The 2021 triple-intersection paper gives closely related sharp estimates, so implicit earlier coverage of the multiplicities or orbit cannot be excluded definitively. Independent validation has not been performed.

## References
1. J. Zhou and H. Wu, *Covering finite fields by translates of multiplicative subgroups*, arXiv:2610.25228v1 (2026-10-18), https://arxiv.org/html/2610.25228v1.
2. A. E. Brouwer and W. J. Martin, *Triple intersection numbers for the Paley graphs*, arXiv:2109.03654v1 (2021), https://arxiv.org/html/2109.03654v1.
3. A. E. Brouwer, *Paley graphs*, section “Dominating sets”, https://aeb.win.tue.nl/graphs/Paley.html.
