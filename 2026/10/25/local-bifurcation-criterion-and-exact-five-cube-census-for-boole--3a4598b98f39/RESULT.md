# Local bifurcation criterion and exact five-cube census for Boolean-to-diamond bounded morphisms

## Finding
For a Boolean inclusion lattice \(B_n=\bigl(2^{[n]},\subseteq\bigr)\) and the four-world Boolean diamond \(D=\bigl(2^{\{a,b\}},\subseteq\bigr)\), both regarded as reflexive Kripke frames, a globally surjective bounded morphism is determined by two monotone Boolean functions. We prove a complete criterion using only the *immediate successors of the maximal common zero points*. This makes the first non-chain Boolean target amenable to exact enumeration.

For \(n=1,2,3,4,5\), the numbers of labelled surjective bounded morphisms are respectively
\[0,\quad2,\quad30,\quad1086,\quad288524.\]
Modulo independent automorphisms of source and target, the numbers of maps are
\[0,\quad1,\quad5,\quad50,\quad1918.\]
Existence holds exactly when \(n\ge2\). Counts are of functions between fixed labelled partially ordered sets; the orbit counts identify functions under relabelling of source atoms and interchange of the two target atoms.

## Assumptions and scope
Fix an integer \(n\ge1\). Source worlds are all subsets of \([n]\); target worlds are \(\varnothing,\{a\},\{b\},\{a,b\}\). Accessibility in both frames is inclusion, including equality. A bounded morphism \(f\) satisfies: (forth) \(x\subseteq y\Rightarrow f(x)\subseteq f(y)\); (back) for every \(x\) and every target world \(t\supseteq f(x)\), some \(y\supseteq x\) satisfies \(f(y)=t\). Globally surjective means every target world has a preimage.

Define monotone \(F(x)={\bf1}_{\{a\in f(x)\}}\), \(G(x)={\bf1}_{\{b\in f(x)\}}\), their truth upsets \(U=F^{-1}(1)\) and \(V=G^{-1}(1)\), and the downset \(Z=B_n\setminus(U\cup V)\). For \(z\subsetneq[n]\), write \(\operatorname{Cov}(z)=\{z\cup\{i\}:i\in[n]\setminus z\}\). Maximality in \(Z\) refers to inclusion.

## Proof
**Normal form.** Forth is equivalent to both \(F,G\) being monotone, because inclusion in the four-world target is the coordinatewise Boolean order. If a map is globally onto and monotone, its bottom image is \(\varnothing\) and its top image is \(\{a,b\}\). Conversely, imposing these endpoint values ensures images at the bottom and top but does not alone ensure either atomic image.

**Necessity of boundary bifurcation.** Let \(z\in\operatorname{Max}(Z)\). Back applied at \(z\) to \(\{a\}\) gives \(y\supseteq z\) with \((F(y),G(y))=(1,0)\). Choose a saturated Boolean-lattice chain from \(z\) to \(y\). Since \(z\) is maximal in \(Z\), its first successor is not a zero point. Monotonicity and \(f(y)=\{a\}\) force that first successor to have image \(\{a\}\), rather than \(\{b\}\) or \(\{a,b\}\). Similarly back to \(\{b\}\) supplies a different immediate successor of image \(\{b\}\).

**Sufficiency.** Assume monotonicity, both endpoint conditions, and the stated two distinct successor colours at every maximal \(z\in Z\). For any zero point \(x\in Z\), choose a maximal \(z\in Z\) above \(x\). The two prescribed successors of \(z\) then witness the back condition at \(x\) for \(\{a\}\) and \(\{b\}\). The top source point witnesses it for \(\{a,b\}\); taking \(y=x\) witnesses it for \(\varnothing\). At a source point with image \(\{a\}\) or \(\{b\}\), the only larger target image is \(\{a,b\}\), witnessed by the source top point, while its own image is witnessed by itself. At a point with top image only reflexivity needs checking. Thus back holds everywhere. The bottom, top, and two boundary successors prove global surjectivity.

**All-dimensional exact enumerator.** Let \(\mathcal U_n^*\) denote the upsets of \(B_n\) which contain \([n]\) but exclude \(\varnothing\). For \(U,V\in\mathcal U_n^*\), let \(Z=B_n\setminus(U\cup V)\). The exact number of labelled bounded surjections is
\[
N_n=\sum_{U,V\in\mathcal U_n^*}\ \prod_{z\in\operatorname{Max}(Z)}
{\bf1}\!\left(\operatorname{Cov}(z)\cap(U\setminus V)\ne\varnothing\right)
{\bf1}\!\left(\operatorname{Cov}(z)\cap(V\setminus U)\ne\varnothing\right).
\]
This expression is finite in every dimension and uses no unproved recurrence or asymptotic assumption: it sums over the Dedekind antichain/upset family and tests the proved boundary normal form. It is not claimed to be a closed-form evaluation as \(n\to\infty\).

**Existence threshold.** A surjection onto four worlds requires at least four source worlds, excluding \(n=1\). For each \(n\ge2\), the coordinate projection \(x\mapsto x\cap\{1,2\}\), after relabelling the target atoms, is a surjective bounded morphism: any enlargement of its target image can be obtained by adding the requested source atoms. Thus the threshold is sharp.

**Finite exact counts.** The standalone program `count_diamond.c` recursively enumerates all monotone Boolean functions (using the decomposition into a lower and an upper \((n-1)\)-cube and their inclusion constraint), tests every ordered pair by the normal form, and counts them exactly for \(n\le5\). `count_diamond_orbits.c` recomputes these counts and uses Burnside's lemma for the action of \(S_n\times S_2\); source permutations permute coordinates, and the target involution swaps the two truth functions. Integer fixed-point totals are divided exactly by \(2n!\). `direct_check.py` independently enumerates all possible truth tables and checks the original forth-and-back definition directly for \(n\le4\), including a separate Burnside evaluation. All independently overlapping values agree.

## Verification
Reproduce using a standard C compiler and Python 3, from the accompanying sources:

```sh
cc -std=c11 -O2 -Wall -Wextra count_diamond.c -o count_diamond
./count_diamond
cc -std=c11 -O2 -Wall -Wextra count_diamond_orbits.c -o count_diamond_orbits
./count_diamond_orbits
python3 direct_check.py
```

The exact, unmodified expected outputs are in `diamond_output.txt`, `orbit_output.txt` and `direct_output.txt`. Complete function-pair enumeration reaches \(n=5\); direct definition checking reaches \(n=4\). The programs do not claim or test any larger dimension, and integer arithmetic remains exact on the tested range.

## Relationship to prior work
The concept of a bounded Kripke morphism and its preservation properties are standard. Figallo–Pascual–Ziliani (2012) study morphisms in the richer setting of monadic augmented Kripke frames, with additional equivalence relations and a duality theorem, not this finite Boolean-to-diamond classification or its orbit census. Sano–Virtema (first posted 2015) study closure under bounded morphic images in modal definability, not counts for a fixed source/target. Kudinov–Shapirovsky (2015) investigate partitionings of finite-height frames; its abstract does not assert these numbers. None of these broader themes alone implies the local two-way cover criterion or the computed five-cube counts. The latter references were inspected at abstract level, not represented as full-text comparisons.

## Limitations
The all-dimensional result is a structural criterion plus a finite sum, not a simple closed form for \(N_n\). The stated numerical counts are rigorously exhaustive only for \(1\le n\le5\), and the independent direct checker reaches \(n\le4\). The searches do not certify absolute publication priority; specialized p-morphism enumerations and unindexed databases remain a residual risk. A separate independent scientific audit has not been performed.

## References
1. A. V. Figallo, I. Pascual, A. Ziliani, *Monadic distributive lattices and monadic augmented Kripke frames*, arXiv:1203.6059 (first posted 2012-03-27), especially definitions and section 3.
2. K. Sano, J. Virtema, *Characterising Modal Definability of Team-Based Logics via the Universal Modality*, arXiv:1502.07884 (first posted 2015-02-27), abstract and bibliographic record.
3. A. Kudinov, I. Shapirovsky, *On partitioning Kripke frames of finite height*, arXiv:1511.09092 (first posted 2015-11-29), abstract and bibliographic record.
4. *p-morphism*, PlanetMath, https://planetmath.org/pmorphism (standard definition).
