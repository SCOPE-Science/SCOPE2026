# Sharp strong odd coloring transition and complete optimal-coloring census of fan graphs

## Finding
Let \(F_n=K_1\vee P_n\) be the fan on a distinguished apex and an ordered, labeled path of \(n\ge2\) vertices. The strong odd chromatic number of a graph is the minimum palette size in a proper coloring for which every color occurring in the open neighborhood of any vertex occurs there an odd number of times.

The exact fan strong odd chromatic number is
\[
\chi_{\mathrm{so}}(F_n)=\begin{cases}
n+1,&2\le n\le6,\\
4,&n\ge7,\quad n\equiv3\pmod6,\\
5,&n\ge7,\quad n\text{ even},\\
6,&n\ge7,\quad n\text{ odd and }n\not\equiv3\pmod6.
\end{cases}
\]

Write \(A_{n,k}\) for the number of path words of length \(n\) on a fixed labeled alphabet of \(k\) symbols such that every color occurs an odd positive number of times and no two equal symbols are at distance one or two. The number \(N_n\) of minimum-color strong odd colorings of \(F_n\) using a fixed, named palette of exactly \(\chi_{\mathrm{so}}(F_n)\) colors is
\[
N_n=\begin{cases}(n+1)!,&2\le n\le6,\\
(k+1)A_{n,k},&n\ge7,\quad k=\chi_{\mathrm{so}}(F_n)-1.\end{cases}
\]
Every coefficient is given explicitly by the following **rational** generating functions, with \(H_k(t)=\sum_{n\ge2} A_{n,k}t^n\):
\[
H_3(t)=\frac{6t^3}{1-t^6};\qquad
H_4(t)=\frac{24t^4(1-2t^2)^2}
{(1-4t^2)\bigl(1-(4t^3-t)^2\bigr)(1+t^2-4t^4)};
\]
\[
H_5(t)=\frac{120t^5(1-3t^2)^3}
{(1-9t^2)\bigl(1-(9t^3-2t)^2\bigr)
\bigl((1+2t^2-9t^4)^2-(t-3t^3)^2\bigr)}.
\]
For example, the exact counts \((N_7,N_8,N_9,N_{10},N_{11},N_{12})\) are \((720,120,24,2400,142560,13080)\).

## Assumptions and scope
Every graph is finite, undirected and simple. The path vertices are distinctly labeled and ordered; color names are also distinguished. A named coloring uses every color of its specified optimal palette. We count full vertex colorings, not equivalence classes under graph automorphisms, reversal of the path, or permutation of color names. The variable \(t\) is formal, so the identities are equalities of formal power series over the rationals. Values \(A_{n,k}\) include only words using all \(k\) colors an odd positive number of times.

## Proof
**1. Structural equivalence.** The apex is adjacent to all path vertices, so its color is private in any proper coloring. At the apex, the strong odd condition requires each path color to occur an odd number of times. Every two path vertices at path distance two share the middle path vertex and the apex in their open neighborhoods. If they had equal colors, those two neighbors would each see this color twice, which is prohibited. Thus the path colors are distinct at distance at most two. Conversely, assume this distance-two condition, odd multiplicity for each used path color, and a private apex color. For an interior path vertex, its two path neighbors have distinct colors and the apex color is different from both, so each is seen exactly once. Endpoints see two distinct colors, each once. The apex sees every used path color an odd number of times. Hence the fan coloring is strong odd exactly under the stated conditions.

**2. Chromatic threshold and six-step extension.** If \(2\le n\le6\), a color repeated on the path must have at least three occurrences (its positive count is odd), with successive occurrences separated by at least three positions. Three occurrences require at least seven positions; therefore all path colors are different, yielding \(n+1\) colors. For \(n\ge7\), the distance-two constraint forces at least three path colors. With exactly three, every valid word is \(123123\cdots\) up to color permutation, because each next symbol is forced by the preceding two. All three multiplicities are odd precisely when \(n\equiv3\pmod6\). As every used path color occurs an odd number of times, the number of used path colors has the same parity as \(n\). Thus, outside the three-color case, an even \(n\) needs at least four path colors and an odd \(n\) needs at least five. These bounds are attained by the following **zero-based** path color words for \(n=7,8,9,10,11,12\), respectively:

```
0120340
01201301
012012012
0120120123
01201201234
012013023123
```

All these words start in `012`. Prepending the six-character block `012012` preserves distance-two properness across the boundary and increases the multiplicities of colors `0`, `1`, `2` by two each. It therefore preserves the odd-multiplicity property and the number of used colors. Iterating gives every \(n\ge7\), proving the chromatic classification.

**3. Exact number of optimal colorings.** Fix \(k\) named path colors. Each permissible path word uniquely defines a strong odd coloring once one of the \(k+1\) named full-palette colors is chosen for the apex; the path alphabet is then the remaining \(k\) colors. This is the bijection \(N_n=(k+1)A_{n,k}\). For \(n\le6\), all \(n+1\) graph vertices have distinct colors, giving \((n+1)!\).

**4. Parity Fourier projection and four-state transfer.** Assign each of the \(k\) path symbols a formal sign \(\varepsilon_j\in\{+1,-1\}\). The indicator that every symbol has odd multiplicity in a word \(w\) is exactly
\[
2^{-k}\sum_{\varepsilon\in\{\pm1\}^k}
\left(\prod_{j=1}^k\varepsilon_j\right)
\prod_{i=1}^{|w|}\varepsilon_{w_i}.
\]
This equality holds because, after multiplication, the sum factors as a product of parity indicators. For a sign assignment with \(a\) positive colors and \(b\) negative colors, \(a+b=k\), the path word's signed weight can be evaluated by a **four-state** transfer indexed by the signs \((g,h)\) of the last two chosen symbols. Let \(m_+=a\), \(m_-=b\), \(s_+=1\), \(s_-=-1\). The signed weight of the first two symbols of types \((g,h)\) is
\[
v_{g,h}=s_gs_h\,m_g\bigl(m_h-\mathbf1_{g=h}\bigr).
\]
The transfer from state \((g,h)\) to \((h,u)\) has weight
\[
M_{(g,h),(h,u)}=s_u\bigl(m_u-\mathbf1_{u=g}-\mathbf1_{u=h}\bigr),
\]
where all other transitions are zero. The subtractions enforce that the newly chosen symbol differs from each of the two previous **individual** symbols, including when their sign types agree. With \(\mathbf 1\) the all-ones column, the generating function of signed distance-two-proper words with this fixed sign partition is
\[
T_{a,b}(t)=t^2 v(I-tM)^{-1}\mathbf1.
\]
Consequently, for each \(k\in\{3,4,5\}\), the exact counting series is
\[
H_k(t)=2^{-k}\sum_{b=0}^{k}(-1)^b\binom{k}{b}T_{k-b,b}(t).
\]
Evaluating these four-by-four rational matrices, summing, and clearing denominators yields precisely the displayed three rational functions. An independent exact-integer determinant-identity checker is included as `verify.py`: it checks the rational equalities by polynomial cross multiplication for each \(k\), with no floating-point operations. The transfer derivation proves the expressions for all lengths, not only those enumerated computationally.

## Verification
Run `python3 verify.py` from this directory using only the Python standard library. It constructs the four-state signed transfer matrices for each of \(k=3,4,5\), evaluates rational matrix functions by determinant identities, and verifies exact polynomial cross-products against the stated closed expressions. An independently coded dynamic program enumerates path words by their last two colors and multiplicity parity mask; its coefficients agree with the rational generating functions through length \(25\). The program also checks all six base words and their six-step extensions through length \(42\). These finite checks support the already complete structural and formal-power-series proofs.

## Relationship to prior work
Kwon and Park introduced strong odd coloring (arXiv:2401.11653, initial public version 22 January 2024). Caro, Petruševski, Škrekovski, and Tuza (arXiv:2410.02336, initial public version 3 October 2024) explicitly observed \(\chi_{\mathrm{so}}(F_6)=7\), so that individual instance is **not new**. Their planar and structural theorems do not give this all-length path-join classification or optimal-coloring generating functions. Manattu, Vinay, and Lakshmanan (arXiv:2602.03259) determined corresponding *chromatic numbers* for joins of cycles and empty graphs, notably wheels. An existing wheel optimal-coloring census concerns \(K_1\vee C_n\), with cyclic closing constraints; these do not supply the distance-two **path** word counts. For example, the fan with nine path vertices has 24 named optimal colorings, whereas the wheel with eight rim vertices belongs to a different graph and counting problem. Results on dissociation polynomials of fans use a different vertex-subset invariant. A 2026 complexity study by Pradhan, Sharma, and Verma (arXiv:2610.01441) addresses algorithmic complexity and a block-graph subclass; fans of larger order are not block graphs. These distinctions do not establish publication priority against every possible source.

## Limitations
This classifies only fan graphs and **named minimum-color** strong odd colorings, not all nonoptimal proper colorings. No new wheel chromatic theorem is claimed. The finite verification ranges do not establish the infinite formulas by themselves; the proof requires the exact transfer identity. A potentially relevant published general paper on strong odd coloring (Pang–Miao–Fan, *Discrete Mathematics*, DOI 10.1016/j.disc.2025.114683) could not be fully inspected despite attempts to locate lawful full text. Its possible specialized coverage, as well as other unindexed literature, remains an originality risk.

## References
1. H. Kwon and B. Park, *Strong odd coloring of sparse graphs*, arXiv:2401.11653, first posted 2024-01-22, https://arxiv.org/abs/2401.11653.
2. Y. Caro, M. Petruševski, R. Škrekovski and Z. Tuza, *On strong odd colorings of graphs*, arXiv:2410.02336, first posted 2024-10-03, https://arxiv.org/abs/2410.02336.
3. A. J. Manattu, A. Vinay and A. Lakshmanan S., *On a conjecture about the strong odd chromatic number of planar graphs*, arXiv:2602.03259, first posted 2026-02-03, https://arxiv.org/abs/2602.03259.
4. D. Pradhan, V. Sharma and S. Verma, *On the Classical and Parameterized Complexity of Strong Odd Coloring*, arXiv:2610.01441, first posted 2026-10-01, https://arxiv.org/abs/2610.01441.
5. Pang, Miao and Fan, *On odd and strong odd colorings of graphs*, *Discrete Mathematics*, DOI 10.1016/j.disc.2025.114683 (full text not inspected).
