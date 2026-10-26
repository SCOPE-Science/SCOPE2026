# Exact modal-operator spectra on finite powers of the three-element Kleene algebra

## Finding
Let \(\mathbf K_3=\{-1,0,1\}\), with its usual order, lattice meet and join given by minimum and maximum, and De Morgan negation \(\sim t=-t\). On the \(n\)-fold direct power \(A_n=\mathbf K_3^n\), \(n\ge1\), consider unary operations \(\Box:A_n\to A_n\) satisfying all three modal-Kleene axioms of Celani, Menchón and Miguelez:

\[
\begin{aligned}
\Box(x\wedge y)&=\Box x\wedge\Box y&&\text{(MK)},\\
\sim\Box(z\vee\sim z)&\leq\Box(z\vee\sim z)&&\text{(Pos)},\\
\Box(x\vee(z\wedge\sim z))&\leq \Box x\vee\sim\Box(x\vee(z\wedge\sim z))&&\text{(Con)}.
\end{aligned}
\]

All operations are counted **on the fixed, coordinate-labelled carrier**; there is no quotient by automorphisms. The exact number of modal-Kleene operations, and the number that are normal (meaning \(\Box\mathbf1=\mathbf1\)), are respectively

\[
\boxed{M_n=(3^n+2^n)^n,\qquad N_n=3^{n^2}.}
\]

Each output coordinate has a unique two-threshold normal form described below. Consequently, the proportion that are normal approaches one, with the sharper asymptotic

\[
1-\frac{N_n}{M_n}\sim n\left(\frac23\right)^n \qquad(n\to\infty).
\]

This theorem includes the structural classification, not only the two numerical formulas.

## Assumptions and scope
For vectors, the order, lattice operations, and involution are all coordinatewise. Write \(\mathbf0=(0,\ldots,0)\), \(\mathbf1=(1,\ldots,1)\), and \(\mathbf b=(-1,\ldots,-1)\); the distinguished bottom of the bounded lattice is \(\mathbf b\), **not** \(\mathbf0\). For \(a\in A_n\), set \(\uparrow a=\{x\in A_n:x\ge a\}\).

For a scalar component \(g:A_n\to\mathbf K_3\), the unique possibilities are:

**Type I (never outputs \(1\)).** Select \(a\in\{-1,0\}^n\), and put
\[
g(x)=\begin{cases}0&x\ge a,\\-1&x\not\ge a.\end{cases}
\]

**Type II (does output \(1\)).** Select \(a\in\{-1,0\}^n\) and \(b\in\{-1,1\}^n\) such that \(a\le b\), and put
\[
g(x)=\begin{cases}1&x\ge b,\\0&x\ge a\text{ and }x\not\ge b,\\-1&x\not\ge a.\end{cases}
\]

These two types are disjoint. The full operator \(\Box\) is any independent selection of such a scalar component for each of its \(n\) output coordinates. Normality is equivalent to the absence of Type I components.

## Proof
**1. Reduction to scalar meet homomorphisms.** Since product meet, join, order and involution are coordinatewise, the three defining axioms hold for \(\Box\) if and only if they hold for every scalar component \(g_i(x)=(\Box x)_i\), with the involution of its scalar value interpreted as \(t\mapsto-t\). Thus components may be classified independently and their counts multiplied.

**2. All scalar meet homomorphisms have two filter thresholds.** Fix a scalar map \(g\) preserving binary meets. It is monotone because \(x\le y\) implies \(g(x)=g(x\wedge y)=\min(g(x),g(y))\). Both upper level sets
\[
F_0=\{x:g(x)\ge0\},\qquad F_1=\{x:g(x)=1\}
\]
are upward closed and closed under nonempty finite meets, hence are either empty or principal upper filters on the finite lattice \(A_n\). Moreover \(F_1\subseteq F_0\). Conversely, any nested choice of such filters defines a unique meet-preserving map to the three-element chain, assigning values \(-1,0,1\) according to filter membership. This establishes uniqueness at the level of the actual function, including constant maps.

**3. Positivity fixes the lower threshold.** Every \(z\vee\sim z\) is coordinatewise nonnegative, and \(z=\mathbf0\) gives \(z\vee\sim z=\mathbf0\). By monotonicity, (Pos) holds exactly when \(g(\mathbf0)\ge0\). Hence \(F_0\ne\varnothing\), and its unique generator \(a\) satisfies \(a\le\mathbf0\), i.e. \(a\in\{-1,0\}^n\).

**4. Consistency forbids zero coordinates in the upper threshold.** Every vector \(t=z\wedge\sim z\) lies in \(\{-1,0\}^n\), and every vector in this subcube is realizable by such a \(z\). Put \(y=x\vee t\). Because \(y\ge x\), the scalar inequality in (Con),
\[
g(y)\le\max(g(x),-g(y)),
\]
is automatic if \(g(y)\le0\), and, if \(g(y)=1\), is equivalent to \(g(x)=1\). If \(F_1\) is empty this imposes no restriction: Type I results.

Otherwise write \(F_1=\uparrow b\), where \(b\ge a\). The consistency requirement becomes
\[
\forall x\in A_n\ \forall t\in\{-1,0\}^n:\quad x\vee t\ge b\ \Longrightarrow\ x\ge b.
\]
If \(b_j=0\) for some coordinate \(j\), take \(x_j=-1\), \(t_j=0\), and every other coordinate of \(x\) equal to \(1\). Then the displayed implication fails (the other coordinates of \(t\) can be set to \(-1\)). Thus all coordinates of \(b\) must be \(-1\) or \(1\). Conversely, if \(b\in\{-1,1\}^n\), any coordinate where \(b_j=1\) can be brought to at least \(1\) by \(x\vee t\) only when \(x_j=1\), since \(t_j\le0\); coordinates where \(b_j=-1\) impose no condition. Therefore the implication always holds. This proves the exhaustive and unique Type II form.

**5. Count.** Type I permits precisely \(2^n\) generators \(a\). For Type II, each input coordinate independently has exactly three choices for \((a_j,b_j)\): \((-1,-1)\), \((-1,1)\), or \((0,1)\). Therefore it permits \(3^n\) threshold pairs. There are \(3^n+2^n\) independent choices for each of \(n\) scalar components, yielding \(M_n=(3^n+2^n)^n\).

For any Type II component, \(g(\mathbf1)=1\); for a Type I component, \(g(\mathbf1)=0\). Hence a full operator preserves the greatest lattice element exactly when all \(n\) components have Type II, yielding \(N_n=(3^n)^n=3^{n^2}\).

Finally \(N_n/M_n=(1+(2/3)^n)^{-n}\). Since \(n(2/3)^n\to0\), the first-order binomial/Taylor expansion gives \(1-N_n/M_n\sim n(2/3)^n\). All assertions follow. \(\square\)

## Verification
The standalone Python 3 file `checker.py` exhaustively tests **every scalar truth table** \(g:A_n\to\mathbf K_3\) for \(n=1\) and \(n=2\), using the three original algebraic axioms, and independently generates all two-threshold tables. It asserts equality of the sets of actual truth tables, not merely numerical agreement. It also counts scalar components sending the top to \(1\). Run `python checker.py`; its complete expected output is:

```text
n=1 scalar=5 normal_scalar=3 full_operators=5 normal_full=3
n=2 scalar=13 normal_scalar=9 full_operators=169 normal_full=81
All exhaustive scalar tables agree with the threshold forms.
```

For \(n=3\) the formulas give \(M_3=42875\) and \(N_3=19683\), but these values are mathematical consequences of the proof, **not** claimed as exhaustively enumerated by the checker. The finite checks support, but do not replace, the general proof.

## Relationship to prior work
Celani, Menchón and Miguelez (2026, arXiv:2608.10937v1) introduce precisely the axioms (MK), (Pos), (Con), and establish a general representation by modal Kleene triples and modal contact structures; see their Definition 3.5 and Theorems 3.13 and 3.18. Those results motivate studying modal operators on the canonical finite Kleene cubes. Their categorical representations do not themselves specify these cube-specific two-threshold forms, their exact numbers, or the asymptotic normality proportion. The present proof uses the axioms directly and counts every permitted operation, including non-normal ones.

Finite-chain studies cover the single three-element chain, where the present formulas recover five admissible operators, three of them normal; they do not classify operations on the non-chain powers \(\mathbf K_3^n\) for \(n\ge2\). Work on "modal Kleene algebras" in the Kleene-star semiring sense concerns a different algebraic signature, and its relational results should not be confused with the De Morgan/Kleene lattices studied here.

## Limitations
The formulas are for the fixed, labelled product \(\mathbf K_3^n\), not for arbitrary finite Kleene algebras or operations counted modulo algebra automorphisms. The asymptotic result concerns uniform counting of admissible operations on the fixed carrier; it is not a statement about random evaluations or random formulas. The independent publication-priority question is not settled by a bounded literature search; unexamined older results on three-valued lattice operators may contain equivalent parameterizations. No independent mathematical audit has been performed.

## References
1. S. Celani, P. Menchón and V. Miguelez, *A Modal Expansion of Kleene Algebras via Twist Structures*, arXiv:2608.10937v1, first posted 2026-08-11. https://arxiv.org/html/2608.10937 and https://arxiv.org/abs/2608.10937.
2. Relevant background on three-valued Kleene logic: *Many-Valued Logic*, Stanford Encyclopedia of Philosophy (Spring 2026 edition), Section 2.2, https://plato.stanford.edu/archives/spr2026/entries/logic-manyvalued/.
