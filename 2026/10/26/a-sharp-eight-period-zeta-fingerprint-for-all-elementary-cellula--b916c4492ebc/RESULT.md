# A sharp eight-period zeta fingerprint for all elementary cellular-automaton images

## Finding

Let \(F_r:\{0,1\}^{\mathbb Z}\to\{0,1\}^{\mathbb Z}\) be the binary radius-one cellular automaton with Wolfram rule \(r\in\{0,\ldots,255\}\), let \(Y_r=F_r(\{0,1\}^{\mathbb Z})\) be its **one-step spatial image**, and let \(\sigma\) be the spatial shift. For every integer \(n\geq1\), put
\[
P_r(n)=\#\{y\in Y_r:\sigma^n y=y\}.
\]
These counts include configurations whose least spatial period divides \(n\); they do not count input configurations or trajectories in time.

**Theorem.** The \(256\) integer sequences \(\big(P_r(n)\big)_{n\geq1}\) fall into exactly **\(31\)** distinct classes. Furthermore,
\[
\big(P_r(1),\ldots,P_r(8)\big)=\big(P_s(1),\ldots,P_s(8)\big)
\quad\Longrightarrow\quad
P_r(n)=P_s(n)\ \text{for every }n\geq1,
\]
and the cutoff \(8\) is sharp. Rules \(7\) and \(25\) have identical counts for all \(1\leq n\leq7\), but \(P_7(8)=148\) while \(P_{25}(8)=156\). Consequently exactly \(31\) distinct Artin–Mazur zeta functions occur among these \(256\) image shifts, and their first eight periodic-point counts are a complete, sharply minimal distinguishing fingerprint within this finite family.

The attached `rule_catalog.csv` assigns each of the \(256\) rules to a class and gives its first eight counts. `class_recurrences.csv` provides for each class an explicit integer linear recurrence which determines the counts **at every positive period** from a finite initial segment. Together the two tables constitute an exact all-period classification, not merely a classification based on truncated computations.

## Assumptions and scope

Rule \(r\) acts at coordinate \(i\) via the bit at index \(4a+2b+c\) in the binary expansion of \(r\), where \((a,b,c)\in\{0,1\}^3\) is the input neighborhood. The source shift is the bilateral full binary shift. Images are taken after one application only. The counting convention is spatial period dividing \(n\) (not necessarily least period \(n\)). For the recurrences below, introduce the *formal* initial value \(P_r(0)=1\); this does not assert the existence of a period-zero orbit.

In `class_recurrences.csv`, a class with coefficients \(c_0=1,c_1,\ldots,c_d\) satisfies
\[
\sum_{j=0}^{d}c_j P_r(n-j)=0\quad(n\geq d).
\]
Thus \(P_r(0),\ldots,P_r(d-1)\), together with the supplied coefficients, determine the entire sequence. The largest displayed recurrence degree is \(56\). The maximum number of reachable Boolean-relation states used for a rule in the exact certificate is \(2375\).

## Proof

**1. Periodic outputs and cyclic Boolean relations.** Use the four predecessor-pair states \(00,01,10,11\). For \(b\in\{0,1\}\), let \(R_b\) be the binary relation containing the transition \((a,c)\to(c,d)\) precisely when the local rule applied to input \((a,c,d)\) gives \(b\). Composition of relations models concatenation of successive output labels. The relation of a word \(w=b_1\cdots b_n\) is \(R_w=R_{b_1}\circ\cdots\circ R_{b_n}\).

A bi-infinite periodic output \(w^\infty\) is in \(Y_r\) **if and only if** the directed graph defined by \(R_w\) contains a directed cycle. Indeed, an input predecessor gives a bi-infinite path on the four-pair graph respecting the infinitely repeated labels, hence a bi-infinite path in its finite \(n\)-phase graph; this graph must contain a directed cycle. Conversely, a cycle of \(R_w\) concatenates to a closed predecessor path labeled by a positive power of \(w\), giving a periodic input that maps to \(w^\infty\). Crucially, the predecessor can have spatial period a *multiple* of \(n\); requiring a loop in \(R_w\) would incorrectly exclude valid outputs.

**2. Exact counting automaton.** Let \(\mathcal R_r\) consist of all Boolean relations reachable from the identity relation \(I\) by right-composition with \(R_0,R_1\). This set is finite, as there are only \(2^{16}\) binary relations on four states. Construct the \(|\mathcal R_r|\)-square nonnegative integer matrix \(T_r\), whose \((U,V)\)-entry counts the labels \(b\in\{0,1\}\) with \(U\circ R_b=V\). Let \(e_I\) be the row concentrated at \(I\), and let \(f_r(U)\) be \(1\) when \(U\) has a directed cycle and \(0\) otherwise. The first step proves the **exact** identity
\[
P_r(n)=e_I T_r^{\,n}f_r\quad(n\geq1).
\]
Its extension to \(n=0\) gives \(P_r(0)=1\), since \(I\) contains loops. No finite-ring injectivity, same-period-predecessor assumption, or asymptotic extrapolation is involved.

**3. An infinite-proof certificate from finitely many integer identities.** Let \(N=|\mathcal R_r|\), and read the recurrence vector \((c_0,\ldots,c_d)\) assigned to \(r\) by the attached tables. Its defect is
\[
Q_r(k)=\sum_{j=0}^{d}c_jP_r(k+d-j)
=e_I T_r^k\Big(\sum_{j=0}^{d}c_jT_r^{d-j}\Big)f_r,
\quad k\geq0.
\]
The exact verifier builds \(T_r\) implicitly, computes the integer periodic-output counts, and checks \(Q_r(k)=0\) for **each** \(k=0,\ldots,N-1\). By Cayley–Hamilton, the sequence \(Q_r(k)\) obeys a homogeneous linear recurrence of order at most \(N\). The checked \(N\) initial zero values therefore imply \(Q_r(k)=0\) for *all* \(k\geq0\). This certifies each supplied recurrence at every integer period. The verifier also checks that within a class the recurrence coefficients and all initial terms through \(P_r(d-1)\) coincide; hence its members have equal periodic-point counts for every \(n\geq1\).

**4. Sharp class separation.** The exact catalog contains all \(256\) rules and exactly \(31\) class labels. Its \(31\) distinct length-eight count vectors distinguish the classes. In particular, equal first eight counts force membership in the same class, and Step 3 then forces equal counts at all periods. The two rows for Rules \(7\) and \(25\) have the same first seven values \((2,4,5,12,22,43,79)\), but their eighth values are \(148\) and \(156\), respectively. Thus no cutoff below eight works.

**5. Zeta-function implication.** By definition, the Artin–Mazur zeta function is the formal power series
\[
\zeta_r(z)=\exp\left(\sum_{n\geq1}\frac{P_r(n)}n z^n\right).
\]
Equality of two such series is equivalent to equality of every \(P_r(n)\), as follows from the formal logarithm. The classification and sharp distinguishing cutoff therefore apply unchanged to zeta functions. Rationality itself is a general property of sofic shifts, not asserted as a new theorem here; the contributed data are the \(31\) **exact rule-specific sequences** and the sharp eight-term fingerprint.

## Verification

The package is self-contained: run `python verify.py` from any directory with `verify.py`, `rule_catalog.csv`, and `class_recurrences.csv` in one folder. It uses only the Python standard library, reconstructs every underlying relation and reachable state, recomputes integer counts, and performs the Cayley–Hamilton certificate checks described above for all \(256\) rules. It separately checks periods \(1\) through \(8\) by enumerating binary output words and seeking directed cycles in a distinct expanded-phase graph, without using Boolean-relation composition for that check.

A successful execution prints:

```
VERIFY_OK: 256 exact complete-state recurrence certificates;
31 pairwise distinct all-period spectra separated by periods <=8;
sharp period-8 witness: Rule 7 versus Rule 25 (P8=148 versus 156);
max relation states=2375; max recurrence degree=56;
2048 independent expanded-phase periodic-word checks (periods 1..8)
```

The exact recurrence verification, not the separate period-eight enumeration, proves the unrestricted claim. All integer arithmetic is exact and the finite-state bound is mathematical.

## Relationship to prior work

The classical theory of sofic shifts and its Manning–Bowen zeta formula supply general finite-state zeta rationality. Manada and Kashyap, *The Zeta Function of a Periodic-Finite-Type Shift* (2009), give more specialized zeta formulas for periodic-finite-type shifts. These general results do not give the \(256\)-rule classification or a sharp comparison cutoff. Salo, *On von Neumann regularity of cellular automata* (2022), systematically studies elementary-cellular-automaton image conditions and periodic-preimage obstructions, but does not give the all-period image-output counts or their \(31\) classes. A previously computed rule-specific spatial zeta function, including the Rule 110 case, does not imply the complete family classification or the sharp separation threshold.

The finite graph and Boolean-relation techniques are standard; the evaluated complete spectrum, its recurrence certificates, and the sharp eight-period distinction are the assessed contribution. Searches do not establish historical priority; earlier equivalent comprehensive tables outside the inspected sources remain possible.

## Limitations

This result classifies the **spatial one-step images** of elementary binary radius-one rules, not their temporal periodic orbits, iterated-limit sets, periodic-input image sets with an *equal* period, or larger neighborhoods and alphabets. It classifies equality of zeta functions, not topological conjugacy of the image shifts. The recurrence tables are exact finite certificates requiring execution/inspection of the provided checker; no independent scientific verification is claimed here. The literature comparisons do not eliminate the possibility of an earlier unindexed complete classification.

## References

1. A. Manada and N. Kashyap, *The Zeta Function of a Periodic-Finite-Type Shift*, arXiv:0904.2375v1 (first submitted 2009-04-15), https://arxiv.org/abs/0904.2375.
2. V. Salo, *On von Neumann regularity of cellular automata*, arXiv:2209.13373v1 (2022-09-27), https://arxiv.org/abs/2209.13373.
3. D. Lind and B. Marcus, *An Introduction to Symbolic Dynamics and Coding*, Cambridge University Press (1995), especially the discussion of sofic-shift zeta functions.
