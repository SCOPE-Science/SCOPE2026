# All 276 preconditionals on the five-element pentagon lattice and the 180 non-induced operations

## Finding

Let \(N_5=\{0,a,b,c,1\}\) have order \(0<a<c<1\) and \(0<b<1\), with \(b\) incomparable to \(a,c\). There are exactly **276** operations \(\Rightarrow:N_5^2\to N_5\) satisfying the five preconditional axioms. Partitioned by \(d=0\Rightarrow0\), their numbers are \(16,18,26,36,180\) for \(d=0,a,b,c,1\), respectively. Of these, exactly **96** arise from the standard construction \(x\Rightarrow y=\nu(x)\vee(x\wedge y)\) with an antitone \(\nu\) satisfying \(\nu(1)=0\), leaving **180** genuinely non-induced operations. Exactly **59** preconditionals additionally satisfy modus ponens. An explicit necessary-and-sufficient row normal form is supplied below. These numbers count labelled operations; since the pentagon has trivial lattice automorphism group, they also count operation isomorphism classes.

## Assumptions and scope

This is the ordinary nondistributive pentagon \(N_5\), not the five-element diamond lattice. Its elements are written in index order \((0,a,b,c,1)\). A preconditional is **any** binary operation satisfying, for all elements \(x,y,z\),

\[
\begin{aligned}
(\mathrm P1)&\quad 1\Rightarrow y\le y,\\
(\mathrm P2)&\quad x\wedge y\le x\Rightarrow y,\\
(\mathrm P3)&\quad x\Rightarrow y\le x\Rightarrow(x\wedge y),\\
(\mathrm P4)&\quad x\Rightarrow(y\wedge z)\le x\Rightarrow y,\\
(\mathrm P5)&\quad x\Rightarrow((x\wedge y)\Rightarrow z)\le(x\wedge y)\Rightarrow z.
\end{aligned}
\]

No conditional-identity, semicomplementation, double-negation, residuation or distributivity axiom is assumed. A unary-induced operation here means the stated construction from an **antitone** map \(\nu\) with \(\nu(1)=0\); it does not mean an arbitrary unary-defined presentation.

## Proof

**1. Universal row reduction.** Write \(f_x(y)=x\Rightarrow y\). P3 and P4 imply
\[
f_x(y)=f_x(x\wedge y),\qquad y\le z\Longrightarrow f_x(y)\le f_x(z).
\]
By P1 and P2, \(f_1\) is the identity. Because \(0\wedge y=0\), \(f_0\) is a constant map, say \(f_0(y)=d\). P2 says \(x\wedge y\le f_x(y)\).

Put \(t=x\wedge y\). The P5 inequality is equivalent, for every comparable pair \(t\le x\), to
\[
f_x(f_t(z))\le f_t(z)\qquad(\text{all }z).
\]
Indeed every such \(t\) is realized by \(y=t\). On the pentagon, after discarding the automatic cases \(x=1\), \(t=x=0\), these inequalities are exactly: (i) each interior row \(f_x\), \(x\in\{a,b,c\}\), satisfies \(f_x(f_x(z))\le f_x(z)\); (ii) \(f_x(d)\le d\) for all three interior rows; and (iii) \(f_c(f_a(z))\le f_a(z)\) for all \(z\). These conditions are thus jointly necessary and sufficient for P1–P5 when coupled to the row reductions.

**2. Complete list of interior self-admissible rows.** Encode a row by its five outputs in the index order \((0,a,b,c,1)\), using digits \(0,1,2,3,4\) for \((0,a,b,c,1)\). Before P5 the permitted rows are obtained by choosing isotone, inflationary values on the meet-ideal \(\mathord\downarrow x\), since \(f_x(y)=f_x(x\wedge y)\). Enforcing the self-absorption inequality in step 1 yields exactly the following finite lists (the displayed digits are *codes*, not arithmetic quantities):

\[
\begin{array}{c|l}
\text{antecedent}&\text{permitted encoded rows}\\\hline
a&01011,\ 03033,\ 04044,\ 11111,\ 24244,\ 33333,\ 44444\\
b&00202,\ 00404,\ 11414,\ 22222,\ 33434,\ 44444\\
c&01033,\ 01044,\ 03033,\ 04044,\ 11133,\ 11144,\ 24244,\ 33333,\ 44444
\end{array}
\]

For direct reproduction without trusting a list, the \(a\)-row is determined by \((f_a(0),f_a(a))\), the \(b\)-row by \((f_b(0),f_b(b))\), and the \(c\)-row by \((f_c(0),f_c(a),f_c(c))\). The inequalities \(x\wedge y\le f_x(y)\), consequent isotonicity, and \(f_x(f_x(y))\le f_x(y)\) select precisely the listed \(7,6,9\) rows; there are no other entries or choices.

**3. Exact census.** For fixed \(d\), filter each displayed row by \(f_x(d)\le d\), and retain \((a,c)\)-row pairs satisfying \(f_c(f_a(z))\le f_a(z)\) at the five possible \(z\). The \(b\)-row is otherwise independent. The resulting entirely explicit table is

| \(d\) | allowed \(b\)-rows | allowed \((a,c)\)-pairs | preconditionals | satisfying modus ponens |
|---|---:|---:|---:|---:|
| \(0\) | 2 | 8 | 16 | 10 |
| \(a\) | 3 | 6 | 18 | 6 |
| \(b\) | 2 | 13 | 26 | 7 |
| \(c\) | 4 | 9 | 36 | 8 |
| \(1\) | 6 | 30 | 180 | 28 |
| **Total** | | | **276** | **59** |

Multiplication of the independent \(b\)-row and admissible \((a,c)\)-pair choices proves the complete 276 count. For modus ponens, on the three interior rows the entire 25-instance condition reduces to
\[
a\wedge f_a(0)=0,\quad b\wedge f_b(0)=0,\quad c\wedge f_c(0)=0,\quad c\wedge f_c(a)=a.
\]
The top and bottom rows automatically satisfy modus ponens. Filtering the same explicit row list by these four conditions gives the last column, totaling 59.

**4. Unary-induced subfamily.** An antitone map \(\nu:N_5\to N_5\) with \(\nu(1)=0\) induces a preconditional \(f_x(y)=\nu(x)\vee(x\wedge y)\) (the standard precomplementation construction). Its negation row gives \(f_x(0)=\nu(x)\); hence distinct such maps yield distinct binary operations. Fix \(d=\nu(0)\), and set \(D=\mathord\downarrow d\). Then \(\nu(a),\nu(b),\nu(c)\in D\), with the only further interior comparison \(\nu(c)\le\nu(a)\). Thus the number of maps with fixed \(d\) is
\[
|D|\cdot|\{(u,v)\in D^2:v\le u\}|.
\]
For \(d=0,a,b,c,1\) this gives \(1,6,6,18,65\), respectively. Their sum is **96**. Subtracting from 276 proves that precisely **180** preconditionals are not obtained from an antitone precomplementation via the displayed formula.

The lattice automorphism group is trivial: \(b\) is the unique atom not below a second non-top element, and the remaining chain \(0<a<c<1\) is fixed. Hence the labelled and isomorphism counts coincide.

## Verification

The accompanying dependency-free `checker.py` constructs the lattice order, joins and meets, enumerates **5,250** row-reduced operation candidates, and independently tests each candidate against the original five axioms, including all instances of P5. A separate enumeration from the exact normal form is compared as a set, not merely by total size. The code independently counts the antitone maps and modus-ponens cases, reporting `ALL_CHECKS_OK K=276 precomp_induced=96 genuinely_noninduced=180 MP=59 T=15 F=5`. The T/F counts are only regression checks, not priority claims. Run `python3 checker.py` from the extracted finding directory. The proof and complete row enumeration, rather than extrapolation from finite experiments, establish the stated facts; here the entire domain is finite and exhaustively covered.

## Relationship to prior work

Holliday's *Preconditionals* gives the axioms and the unary precomplementation construction. Chen's July 2026 *Fundamental Propositional Logic with Preconditional* characterizes the \(\mathsf K\), \(\mathsf T\), and \(\mathsf F\) algebra classes and proves general metatheorems, without an exact census for the unrestricted \(\mathsf K\) operations on this pentagon in its examined algebraic and model-theoretic sections. The unary-induced construction and the definitions themselves are prior work. The claimed contribution is the **complete unrestricted pentagon census, explicit row classification, exactly 180 non-induced operations and the 59-operation modus-ponens refinement**. The stronger \(\mathsf T/\mathsf F\) subclass counts are not claimed as original findings here.

## Limitations

Only the single five-element pentagon carrier is classified, not arbitrary nondistributive lattices or all long-pentagons. The 276 total concerns actual binary operations, not equivalence under a weaker semantics. The row codes use a fixed indexing and have been cross-checked using direct source axioms. No general asymptotic or decidability theorem follows. Potential equivalent older tabulations or nonstandard naming conventions remain a priority risk; this is a self-review without independent audit.

## References

1. Zhicheng Chen, *Fundamental Propositional Logic with Preconditional: Strong Completeness, Finite Model Property, and Modal Translations*, arXiv:2607.20221, first publicly posted 2026-07-22; Definition 3.1, Lemma 3.2 and Definition 3.3.
2. Wesley H. Holliday, *Preconditionals*, arXiv:2402.02296, initially posted 2024-02-03; Definition 1, Propositions 1–2, and Section 2.3.
