# Ten modulo-eleven residue pairs give one power-free pseudoperiodic family
## Finding
Let \(\mathbf t\) be the Thue--Morse word, and define the \(11\)-uniform morphism
\[
h(0)=\mathtt{11100011000},
\qquad
h(1)=\mathtt{11100111000}.
\]
Set \(\mathbf s=h(\mathbf t)\).

For positive integers \(a<b\), the word \(\mathbf s\) has pseudoperiod \((a,b)\) whenever the unordered pair of residues
\[
\{a\bmod 11,b\bmod 11\}
\]
is one of
\[
\{1,4\},\ \{1,5\},\ \{1,10\},\ \{2,5\},\ \{4,6\},
\]
\[
\{5,6\},\ \{5,7\},\ \{6,9\},\ \{6,10\},\ \{7,10\}.
\]
The same single word \(\mathbf s\) avoids every \(3^+\)-power.

Consequently these ten unordered residue pairs prove the binary pseudoperiod avoidance conjecture for twenty oriented residue classes modulo \(11\). None of those classes can satisfy \(b=2a\). Among all pairs \(1\le a<b\), the certified family has natural density
\[
\frac{20}{121}.
\]

## Assumptions and scope
A binary infinite word \(x=x_0x_1x_2\cdots\) has pseudoperiod \((a,b)\) when
\[
x_i\in\{x_{i+a},x_{i+b}\}
\]
for every \(i\ge0\). A \(3^+\)-power is a factor of exponent strictly greater than \(3\).

Residues in the statement are taken in \(\mathbb Z/11\mathbb Z\), with the displayed representatives \(0,\ldots,10\). The result is a sufficient arithmetic family. It does not claim that the twenty residue classes are all pseudoperiods of \(\mathbf s\), because correlations in the Thue--Morse symbols can create additional pairs beyond the residue-only argument.

## Proof
The two morphism images differ at exactly one zero-based residue:
\[
h(0)=\mathtt{11100\,0\,11000},
\qquad
h(1)=\mathtt{11100\,1\,11000}.
\]
Hence
\[
s_{11q+r}=
\begin{cases}
1,&r\in\{0,1,2,6,7\},\\
0,&r\in\{3,4,8,9,10\},\\
t_q,&r=5.
\end{cases}
\]

This makes the pseudoperiod condition a finite residue check. For residues \(r_a,r_b\), consider a source residue \(u\). Whenever any of
\[
u,\quad u+r_a,\quad u+r_b
\]
equals \(5\), replace the corresponding symbol by an arbitrary independent bit. At every other residue use the fixed symbol above. If, for every \(u\) and every assignment of those arbitrary bits, the source bit equals at least one of the two shifted bits, then every actual Thue--Morse assignment satisfies the pseudoperiod condition.

Exhausting the \(11^2\) ordered residue pairs gives exactly
\[
\begin{aligned}
&(1,4),(1,5),(1,10),(2,5),(4,1),(4,6),\\
&(5,1),(5,2),(5,6),(5,7),(6,4),(6,5),(6,9),(6,10),\\
&(7,5),(7,10),(9,6),(10,1),(10,6),(10,7).
\end{aligned}
\]
These are precisely the two orientations of the ten unordered pairs in the finding. The check treats the variable positions as independent, so it is stronger than any finite-prefix observation and proves the condition for arbitrary quotients of \(a\) and \(b\) by \(11\).

It remains to verify that \(\mathbf s\) avoids \(3^+\)-powers. Suppose a factor has period \(p\) and length \(3p+1\). Then
\[
s_{i+j}=s_{i+j+p}
\qquad
(0\le j\le2p).
\]

First suppose \(11\nmid p\) and \(p\ge5\). Put \(d=p\bmod11\). For every nonzero \(d\), there is a fixed residue \(r\), with neither \(r\) nor \(r+d\) equal to \(5\), on which the two template bits disagree. One choice for \(d=1,\ldots,10\) is
\[
2,1,0,0,8,2,1,0,0,0.
\]
The \(2p+1\) consecutive comparison positions contain every residue modulo \(11\), so one comparison encounters this fixed mismatch, a contradiction.

Now suppose \(11\mid p\), say \(p=11q\). Among the \(2p+1\) comparison positions are at least \(2q\) consecutive positions congruent to \(5\) modulo \(11\). Restricting the equalities to them gives a factor of \(\mathbf t\) of length \(3q\) and period \(q\), hence a cube. This contradicts the classical cube-freeness of the Thue--Morse word.

The remaining periods \(p=1,2,3,4\) are finite. Every factor of \(\mathbf s\) of length at most \(13\) is contained in \(h(v)\) for a length-\(3\) factor \(v\) of \(\mathbf t\). The six possibilities are
\[
\mathtt{001},\mathtt{010},\mathtt{011},
\mathtt{100},\mathtt{101},\mathtt{110}.
\]
Checking all six factors and all eleven starting residues gives no factor of period \(p\) and length \(3p+1\). Thus \(\mathbf s\) is \(3^+\)-power-free.

Finally, none of the twenty successful ordered residue pairs has second coordinate congruent to twice the first modulo \(11\), so no integer pair in the family can have \(b=2a\). Each oriented residue class has asymptotic density \(1/121\) among \(a<b\), giving the stated density \(20/121\).

## Verification
Run `python3 verify.py` beside `certificate.json`.

The verifier reconstructs the \(11\)-residue template directly from the two morphism images and independently tests all \(121\) ordered residue pairs, allowing independent adversarial bits at every variable residue. It recovers exactly the twenty orientations listed in the proof.

It checks the fixed mismatch witness for every nonzero period residue modulo \(11\), reconstructs the six length-\(3\) Thue--Morse factors, and exhausts all short cases \(p=1,2,3,4\). The numbers of distinct candidate factors examined at lengths \(4,7,10,13\) are respectively
\[
8,\ 14,\ 20,\ 26.
\]
A separate finite stress test evaluates every certified pair with \(b\le300\) on a long independently generated prefix of \(h(\mathbf t)\).

The infinite pseudoperiod proof is the adversarial residue argument, and the infinite power-freeness proof uses the fixed mismatch argument plus the classical cube-freeness of Thue--Morse. No finite experiment is promoted to an infinite conclusion.

## Relationship to prior work
Meleshko, Ochem, Shallit, and Shan formulate the conjecture that every pair \(1\le a<b\), \(b\ne2a\), admits an infinite binary word with pseudoperiod \((a,b)\) avoiding \(3^+\)-powers. They verify all pairs with \(b\le54\).

Their paper prints exactly the same morphism \(h\), saying that it was generated for \((1,5)\) and also worked for \(122\) other tested pairs. It verifies \((1,5)\) and \(3^+\)-power-freeness computationally, but it does not give an arithmetic description of all shifts certified by this morphism.

The same paper later proves a positive-density theorem for the one-dimensional family \((1,a)\), using several uniform morphisms and residue classes. That theorem does not imply a two-dimensional residue family for arbitrary \((a,b)\).

The present result extracts a quotient-independent structural property of the printed morphism: twenty complete residue classes modulo \(11\) are certified simultaneously by one word. This converts a finite list of successful tests into an infinite two-parameter family while leaving the full conjecture open.

## Limitations
The residue condition is sufficient, not necessary, for \(\mathbf s\). The actual pseudoperiod set of \(\mathbf s\) may contain additional pairs because the variable residue is governed by Thue--Morse rather than by independent arbitrary bits.

The density \(20/121\) is a density of parameter pairs certified by this one morphic word; it is not a density statement about all solutions of the conjecture.

The result does not characterize pairs outside these residue classes and does not settle the full binary pseudoperiod avoidance conjecture.

## References
1. J. Meleshko, P. Ochem, J. Shallit, and S. L. Shan, “Pseudoperiodic Words and a Question of Shevelev,” arXiv:2207.10171v1, first public version 2022-07-20; Discrete Mathematics & Theoretical Computer Science 25(2), Article 6 (2023), DOI 10.46298/dmtcs.9919.
2. J.-P. Allouche and J. Shallit, *Automatic Sequences: Theory, Applications, Generalizations*, Cambridge University Press, 2003.
