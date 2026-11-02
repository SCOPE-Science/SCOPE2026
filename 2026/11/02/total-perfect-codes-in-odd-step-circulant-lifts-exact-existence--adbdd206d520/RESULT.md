# Total perfect codes in odd-step circulant lifts: exact existence and enumeration

## Finding

Let \(r\ge 2\) and \(n\ge 4r\) be integers. Define the connected simple circulant
\[
G_{n,r}=\operatorname{Cay}\bigl(\mathbb Z_n,\{\pm1,\pm3,\ldots,\pm(2r-1)\}\bigr).
\]
A **total perfect code** is a set \(C\subseteq\mathbb Z_n\) such that every vertex (including those in \(C\)) has **exactly one** neighbor in \(C\). Equivalently, the open neighborhoods centered at \(C\) partition the vertices.

**Theorem.** A total perfect code in \(G_{n,r}\) exists if and only if \(4r\mid n\). If \(4r\mid n\), **every** total perfect code is of the form
\[
C_{a,b}=\{v\in\mathbb Z_n:v\equiv a\text{ or }b\pmod{4r}\},
\quad a\in\{0,2,\ldots,4r-2\},\quad
b\in\{1,3,\ldots,4r-1\}.
\]
These sets are pairwise distinct. Consequently the number of distinct total perfect codes on the named vertex set \(\mathbb Z_n\) is exactly
\[
\#\operatorname{TPC}(G_{n,r})=
\begin{cases}(2r)^2,&4r\mid n,\\0,&4r\nmid n.\end{cases}
\]
Each existing code has exactly \(n/(2r)\) vertices. In particular, the total perfect codes of **every** cyclic lift \(G_{4rk,r}\), for every \(k\ge1\), are precisely the pullbacks of the \((2r)^2\) two-vertex codes of the base graph \(G_{4r,r}\cong K_{2r,2r}\). No additional nonperiodic codes arise on larger lifts.

## Assumptions and scope

The vertices are the named residue classes of \(\mathbb Z_n\). The assumption \(n\ge4r\) makes the \(2r\) specified nonzero odd steps pairwise distinct modulo \(n\), so that \(G_{n,r}\) is simple and \(2r\)-regular. The presence of step \(1\) makes it connected. The theorem classifies **total perfect codes**, also called *efficient open dominating sets*; it is not a classification of ordinary perfect (closed-neighborhood) codes or of arbitrary minimum total dominating sets. It includes all lift factors and does not impose a primality restriction on \(r\) or on \(n/(4r)\).

## Proof

Write \(m=2r\), so \(m\ge4\) is even, and let \(u_j\in\{0,1\}\) be the indicator of a putative total perfect code, with indices read modulo \(n\). The full list of open-neighborhood equations is
\[
T_j:=\sum_{h=0}^{m-1}u_{j-m+1+2h}=1
\quad(j\in\mathbb Z_n).\tag{1}
\]
This is exactly the defining condition: the indices on the left are \(j-(m-1),j-(m-3),\ldots,j+(m-1)\), the \(m\) distinct neighbors of \(j\).

**Step 1 (rigidity of the period).** Equation (1) at \(j+2\) has the same \(m-1\) interior terms as equation (1) at \(j\). Subtracting gives
\[
0=T_{j+2}-T_j=u_{j+m+1}-u_{j-m+1}.
\]
As \(j\) varies, this is precisely
\[
u_{j+2m}=u_j\quad\text{for all }j\in\mathbb Z_n.\tag{2}
\]
Thus **every** total perfect code, before any assumed construction or computation, is invariant under translation by \(2m=4r\).

**Step 2 (arithmetic obstruction).** Sum equation (1) over all \(j\in\mathbb Z_n\). Every selected vertex occurs as a neighbor of exactly \(m\) vertices, yielding
\[
m\sum_j u_j=n.
\]
Thus \(m\mid n\), and every possible code has cardinality \(n/m\). If \(2m\nmid n\), then \(n/m\) is odd, so \(\gcd(n,2m)=m\). By (2) and the ordinary period \(n\), the sequence is then \(m\)-periodic. In a neighborhood sum (1), every odd residue class modulo the even number \(m\) occurs **twice**. Therefore every \(T_j\) is an even integer, contradicting \(T_j=1\). Consequently
\[
2m=4r\mid n
\]
is necessary.

**Step 3 (complete classification).** Assume \(2m\mid n\). By (2), \(u\) is the periodic pullback of its values on \(\mathbb Z_{2m}\). For each \(j\), the \(m\) offsets \(-(m-1),-(m-3),\ldots,m-1\) represent every **odd** residue class modulo \(2m\) exactly once. Thus equation (1) says that, among the \(m\) residue classes of parity opposite to \(j\), exactly one has indicator \(1\). Taking \(j\) even gives exactly one selected odd class; taking \(j\) odd gives exactly one selected even class. No further restrictions exist, since these two conditions imply all equations (1).

There are \(m\) choices for the even class and independently \(m\) choices for the odd class. This proves both the stated form and the exact count \(m^2=(2r)^2\). Every such choice occurs and gives a distinct subset of \(\mathbb Z_n\). Since each selected residue class contains \(n/(2m)\) vertices, the code size is \(n/m\), as required. \(\square\)

## Verification

The included standalone Python 3 program `verify.py` checks the graph definition directly against independent complete enumerators. It performs literal subset enumeration in six small cases (including \((r,n)=(2,8),(2,12),(3,12),(4,16)\)), an independent recurrence-based exhaustive search in 45 parameter cases for \(1\le r\le4\), and direct checks of 7,800 distinct prescribed codes for \(1\le r\le12\) and lift factors \(1,2,3\). The observed results are

```
LITERAL_SUBSET_ENUMERATION_OK 6
SEED_RECURRENCE_ENUMERATION_OK 45
CANONICAL_CONSTRUCTIONS_OK 7800
VERIFY_OK
```

These finite experiments are **not** an exhaustive proof over all parameters. The complete proof above uses equation (1), an exact two-step shift comparison, divisibility, and residue-class counting. To replay, run `python3 verify.py` with standard Python 3; no third-party dependencies are needed.

## Relationship to prior work

The study is motivated by Cameron, Yap, and Zhou's work on perfect and total perfect codes in abelian Cayley graphs (arXiv:2507.11871, first publicly posted July 16, 2025). Their Theorem 5.3 completely classifies total perfect codes when \(n=p|S|\) for prime \(p\); for the present connection set at \(n=4r=2|S|\), that covers the **base** graph \(K_{2r,2r}\). Its Theorems 5.2 and 5.4–5.6 do not state the all-lift assertion above; their subgroup or coprimality assumptions also do not supply the non-subgroup codes displayed here at larger multiples of \(4r\). In particular, the new contribution is **period rigidity and completeness for every cyclic lift**, not the familiar classification of two-vertex codes in the complete bipartite base graph.

Koohestani, Mojdeh, and Ghasemi (arXiv:2510.20376, first publicly posted October 23, 2025) examine total perfect codes of *Cayley sum graphs*. Because the step set here contains only odd elements and \(n\) must be even for a total perfect code, the Cayley difference graph is isomorphic to the corresponding Cayley sum graph: fix each even vertex and negate each odd vertex. This equivalence was explicitly considered in the comparison. Their Theorem 3.4 handles the base-order case \(n=2|S|\), while their later coprime-factor theorems do not cover the candidate orders \(n\) with \(4r\mid n\). They do not state the all-lift classification under this equivalent formulation.

Feng, Huang, and Zhou (arXiv:1703.08652) prove general **existence** criteria for certain circulant perfect and total perfect codes, but not the above full, all-lift enumeration. Obradović, Peters, and Ružić (DOI:10.1016/j.ipl.2007.02.004) concern **ordinary efficient domination**, using closed neighborhoods, rather than the open-neighborhood condition here. The latter paper's complete text was inaccessible for direct comparison; its abstract was consulted. Searches for alternate descriptions, including efficient open domination, circular odd-step graphs, and cyclic tilings, did not identify a covering theorem, but an unsuccessful search is not proof of historical novelty.

## Limitations

This result is specific to the symmetric interval of odd jumps and to the convention \(n\ge4r\). It does not classify total perfect codes of arbitrary circulants or provide a solution for arbitrary step sets. The ordinary perfect-code classification and the complete-bipartite base case are not claimed as new. The proof and code have undergone self-review only; no independent mathematical audit or comprehensive historical-priority certification has been performed. Possible equivalent older formulations, especially under tiling terminology, remain a historical-priority risk.

## References

1. P. J. Cameron, R. S. Yap and S. Zhou, *Perfect codes in Cayley graphs of abelian groups*, arXiv:2507.11871, first posted 2025-07-16; Designs, Codes and Cryptography (2026), DOI:10.1007/s10623-026-01821-1, particularly Section 5 and Theorem 5.3.
2. M. Koohestani, D. A. Mojdeh and M. Ghasemi, *Total perfect codes in Cayley sum graphs of cyclic groups*, arXiv:2510.20376, first posted 2025-10-23, particularly Theorems 3.4, 3.7 and 3.13.
3. R. Feng, H. Huang and S. Zhou, *Perfect codes in circulant graphs*, arXiv:1703.08652, first posted 2017-03-25; Discrete Mathematics 340 (2017), 1522–1527.
4. N. Obradović, J. Peters and G. Ružić, *Efficient domination in circulant graphs with two chord lengths*, Information Processing Letters 102 (2007), 253–258, DOI:10.1016/j.ipl.2007.02.004 (abstract inspected; full text unavailable).
