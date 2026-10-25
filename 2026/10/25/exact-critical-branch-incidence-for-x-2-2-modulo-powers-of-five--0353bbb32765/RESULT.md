# Exact critical-branch incidence for \(x^2-2\) modulo powers of five

## Finding
For every integer \(k\ge1\), put \(R_k=\mathbb Z/5^k\mathbb Z\) and let \(f:R_k\to R_k\) be \(f(x)=x^2-2\). Its functional graph has exactly \(3k-1\) cycle components. The first-entry depth is exactly \(0\), \(1\), or \(2\) according as \(x\bmod5\) belongs to \(\{2,4\}\), \(\{1,3\}\), or \(\{0\}\). Every cycle vertex has exactly one strictly preperiodic predecessor at depth one. The depth-two branches are classified completely by the valuation and quadratic character of the cycle vertex, as follows.

There are fixed cycles at \(2\) and \(-1\). For each \(1\le t<k\), the residues with \(\nu_5(x-2)=t\) form exactly two cycles, one for each value \(\epsilon=\left(\frac{(x-2)/5^t}{5}\right)\in\{-1,1\}\). Both cycles have length \(\ell_t=2\cdot5^{k-t-1}\). The residues with \(\nu_5(x+1)=t\) form exactly one cycle, of length \(m_t=4\cdot5^{k-t-1}\). Valuations of residues are truncated at precision \(k\); here the quoted valuations are exact because \(t<k\), and the Legendre symbol is applied to the nonzero reduction modulo five.

At the fixed vertex \(2\), its unique depth-one predecessor is \(-2\), which has precisely \(5^{\lfloor k/2\rfloor}\) depth-two predecessors. At \(-1\) and at every vertex on any \(m_t\)-cycle, the depth-one predecessor has no depth-two predecessors. At a vertex \(y\) on the \((t,\epsilon)\)-cycle near \(2\), its unique depth-one predecessor has precisely
\[
B(t,\epsilon)=\begin{cases}
2\cdot5^{t/2},&t\text{ even and }\epsilon=1,\\
0,&\text{otherwise}
\end{cases}
\]
depth-two predecessors. Thus **exactly one of the two cycles at every even valuation level receives critical depth-two branches**, and neither cycle at an odd level receives any. All depth-two vertices are leaves.

In particular, the component sizes are \(2+5^{\lfloor k/2\rfloor}\) for the cycle at \(2\), \(2\) for the cycle at \(-1\), \(2m_t\) for each \(m_t\)-component, and \((2+B(t,\epsilon))\ell_t\) for each \((t,\epsilon)\)-component. These formulas specify the complete rooted functional graph up to isomorphism, including component counts, cycle lengths and the number of incoming leaves at each cycle vertex.

## Assumptions and scope
We work with residue classes modulo \(5^k\), with \(k\ge1\), and direct an edge from \(x\) to \(f(x)\). A cycle vertex has depth zero, and a transient vertex has depth equal to the number of iterations before first entering any periodic orbit. A predecessor counted as depth one or two is distinct from the preceding cycle vertex. The map is the monic quadratic Dickson polynomial \(D_2(x,1)\), conjugate under multiplication by \(2\) to the ordinary Chebyshev polynomial \(T_2\) over rings of odd characteristic. This is a nonpermutation map modulo five.

## Proof
**1. Reduction and depth.** Modulo five the map reads
\[
0\mapsto3\mapsto2\mapsto2,\qquad 1\mapsto4\mapsto4,
\qquad 3\mapsto2,
\]
with \(2\) and \(4=-1\) fixed. The restricted maps on the two residue disks \(x\equiv2\) and \(x\equiv-1\pmod5\) are permutations modulo every \(5^k\): indeed \(f'(x)=2x\) is a unit there, and the restriction is bijective by Hensel lifting from its fixed reduction modulo five. Therefore all these residues are periodic, while the other three residue classes enter these periodic disks in exactly one, one and two steps, respectively. In particular, the depth census is \((2\cdot5^{k-1},2\cdot5^{k-1},5^{k-1})\).

**2. The local period-lifting lemma.** Suppose \(g\in\mathbb Z[x]\), \(x\in\mathbb Z\), \(g'(x)\equiv1\pmod5\), and \(h=\nu_5(g(x)-x)\ge2\). Then
\[
\nu_5(g^{\circ j}(x)-x)=h+\nu_5(j)\qquad(j\ge1).
\]
To prove this, write \(\delta=g(x)-x\) and \(a=g'(x)\). Modulo \(5^{h+2}\), the Taylor expansion at \(x\) shows that \(g^{\circ j}(x)-x\equiv\delta(1+a+\cdots+a^{j-1})\) for \(1\le j\le5\), since quadratic error terms have valuation at least \(2h\ge h+2\). As \(a\equiv1\pmod5\), the five-term sum is congruent to \(5\pmod{25}\), hence the fivefold displacement has valuation \(h+1\). A number of iterations prime to five leaves the valuation at \(h\), by the same first-order calculation modulo \(5^{h+1}\). Iterating the fivefold assertion (the derivatives remain \(1\pmod5\) along the orbit) and then the prime-to-five assertion proves the lemma for every \(j\).

**3. Periodic disks.** Set \(x=2+u\) with \(t=\nu_5(u)\ge1\). Since \(f(2+u)=2+4u+u^2\), direct expansion yields
\[
\nu_5(f(x)-x)=t,\qquad \nu_5(f^{\circ2}(x)-x)=t+1.
\]
The second equality also follows from \(f^{\circ2}(x)-x=(x-2)(x+1)(x^2+x-1)\) and \(x^2+x-1=5+5u+u^2\). The derivative of \(f^{\circ2}\) at \(x\equiv2\pmod5\) equals \(16\equiv1\pmod5\). The lemma therefore gives the least period \(2\cdot5^{\max(0,k-t-1)}\) at precision \(k\) for every \(1\le t<k\); the root \(2\) is fixed.

Similarly set \(x=-1+u\), \(t=\nu_5(u)\ge1\). In local coordinates the map is \(u\mapsto-2u+u^2\), whose second iterate has linear term \(4u\) and fourth iterate has the expansion \(16u+40u^2+u^3Q(u)\) with integral polynomial \(Q\). Consequently, the first and second iterate displacements have valuation \(t\), while the fourth iterate displacement has valuation exactly \(t+1\). The derivative of \(f^{\circ4}\) on this disk is \(16\equiv1\pmod5\). The lemma gives least period \(4\cdot5^{\max(0,k-t-1)}\), and \(-1\) is fixed.

At each level \(t<k\) in either disk there are \(4\cdot5^{k-t-1}\) residues. Dividing by the just-proved least periods yields two cycles in the \(2\)-disk and one cycle in the \(-1\)-disk. In the \(2\)-disk, \(f(x)-2=(x-2)(x+2)\) and \(x+2\equiv4\pmod5\), a quadratic residue. Hence the sign \(\epsilon\) is constant along each cycle; each sign class contains \(2\cdot5^{k-t-1}\) vertices, exactly one cycle. This also proves the total \(3k-1\) cycle count.

**4. All incoming branches.** For a periodic \(y\equiv2\pmod5\), solving \(z^2=y+2\) gives exactly two roots modulo \(5^k\), by simple-root Hensel lifting: one root \(z\equiv2\pmod5\) is the periodic predecessor, and the other \(z\equiv-2\pmod5\) is its unique depth-one predecessor. The same argument for a periodic \(y\equiv-1\pmod5\) gives its unique periodic predecessor \(z\equiv-1\pmod5\) and unique depth-one predecessor \(z\equiv1\pmod5\). The latter has no predecessor because \(z+2\equiv3\pmod5\) is a nonsquare.

For a depth-one vertex \(z\equiv-2\pmod5\), depth-two predecessors are precisely the roots \(w\) of \(w^2=z+2\pmod{5^k}\), necessarily with \(w\equiv0\pmod5\). If \(z=-2\), there are exactly \(5^{\lfloor k/2\rfloor}\) roots. Otherwise put \(t=\nu_5(z+2)<k\). A root exists exactly if \(t\) is even and \((z+2)/5^t\) is a quadratic residue modulo five; in that case the number of roots is \(2\cdot5^{t/2}\), by the standard square-root lifting count. If \(y=f(z)\), then
\[
y-2=(z-2)(z+2),\qquad z-2\equiv1\pmod5.
\]
Thus \(t=\nu_5(y-2)\), and the quadratic sign of its normalized unit equals that of \((y-2)/5^t\). This proves exactly the asserted \(B(t,\epsilon)\) and the exceptional fixed-point count. Every depth-two vertex is \(0\pmod5\), so it has no predecessor: \(w+2\equiv2\pmod5\) is a nonsquare. There are no other branches by the reduction step. The component-size formulas follow by adding one depth-one vertex, and the stated number of depth-two leaves, at each cycle vertex.

## Verification
Run `python verify.py` with the Python standard library. The script constructs the entire directed graph independently for \(1\le k\le7\), removes acyclic vertices, explicitly discovers all cycles, assigns first-entry depths using reverse edges, and compares every cycle length and every depth-two attachment against the formulas. It also checks component sizes and the three residue-class depth counts. The executed script returned:

`VERIFY_OK: 97655 distinct residue states across k=1..7; 77 exact cycles; 1633 cycle vertices with depth-two leaves; all tails, periods and component sizes`

This finite enumeration is corroboration, not a proof for all \(k\). The infinite classification is supplied by the modular and valuation arguments above.

## Relationship to prior work
Gassert (2012) classifies monic Chebyshev functional graphs over finite fields, not the residue rings \(\mathbb Z/5^k\mathbb Z\). Diarra and Sylla (2013 preprint), Proposition 15, establish a Siegel-disc description near periodic points of Chebyshev maps of degree prime to the residue characteristic; this does not identify finite-ring preperiodic leaves or their placement among cycles. Li, Lu, Tan and Chen (2022) analyze Chebyshev *permutation* polynomials over odd prime-power residue rings, whereas this quadratic map is not a permutation modulo five. Panraksa and Tangboonduangjit (2026) determine fixed and exact-periodic point counts for Chebyshev maps over odd prime-power rings, including nonpermuting degrees. Their period formulas cover the periodic portion of this example; that portion is not claimed as new here. Their conclusion expressly separates the classification of nonperiodic incoming trees as a further problem. The new result is the complete **cycle-by-cycle incidence and root multiplicity** of the critical depth-two branches, distinguished by the normalized quadratic sign at each valuation level, together with full component sizes. The periodic census is included to state this classification self-containedly.

## Limitations
Only the monic quadratic Dickson map modulo powers of five is classified; the theorem does not solve the incoming-tree problem for other degrees or primes. The proof does not assert novelty of standard Hensel lifting, quadratic-residue root counts, or previously published cycle counts. The literature comparison is subject to the residual possibility of an equivalent unpublished or unlocated specialization. Independent mathematical validation has not been performed.

## References
1. T. Alden Gassert, *Chebyshev Action on Finite Fields*, arXiv:1209.4396v1 (first public posting 2012-09-20), https://arxiv.org/abs/1209.4396.
2. C. Li, X. Lu, K. Tan and G. Chen, *The Graph Structure of Chebyshev Permutation Polynomials over \(\mathbb Z/p^k\mathbb Z\)*, arXiv:2209.14658v1 (2022), https://arxiv.org/abs/2209.14658.
3. B. Diarra and D. Sylla, *p-Adic dynamical systems of Chebyshev polynomials*, preprint dated 2013-03-21, Proposition 15, https://padic2013.mi-ras.ru/Diarra.pdf.
4. C. Panraksa and A. Tangboonduangjit, *Fixed points and exact periods of Chebyshev polynomials modulo odd prime powers*, arXiv:2605.04417v2 (2026), https://arxiv.org/html/2605.04417v2.
