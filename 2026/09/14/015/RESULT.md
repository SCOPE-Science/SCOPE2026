# Irreducibility, atoroidality, index and ideal Whitehead graph of `a -> bc, b -> c, c -> d, d -> a` in `Out(F4)`

## Context

Let `F4 = F(a,b,c,d)` and define

`Phi(a)=bc, Phi(b)=c, Phi(c)=d, Phi(d)=a`.

Let `f` be the corresponding rose map and let `phi` be its outer class.

## Result

`Phi` is an automorphism. Its outer class `phi` is ageometric fully
irreducible and atoroidal. The periodic directions are

`{a,b,c,d,A,C,D}`

(where capital letters denote inverse directions), and the ideal Whitehead
graph is the connected complete bipartite graph `K_{4,3}` with bipartition
`{a,b,c,d}` and `{A,C,D}`. Hence the index list is `[-5/2]`. The power
`f^12` fixes every periodic direction and, because there are no periodic
Nielsen paths, satisfies the standard rotationless train-track condition.

## Exact combinatorial certificate

An explicit inverse is

`a -> d, b -> aB, c -> b, d -> c`.

The unsigned transition matrix in the ordered basis `(a,b,c,d)` is

```
M = [[0,1,1,0],
     [0,0,1,0],
     [0,0,0,1],
     [1,0,0,0]].
```

Direct integer expansion gives `det(M)=-1` and `det(xI-M)=x^4-x-1`. Moreover

```
M^10 = [[3,1,2,3],
        [2,1,1,1],
        [1,2,3,1],
        [1,1,3,3]],
```

so the transition matrix is Perron-Frobenius.

The direction map is

`a->b, b->c, c->d, d->a, A->C, B->C, C->D, D->A`.

There are seven gates: `{a},{b},{c},{d},{A,B},{C},{D}`. Thus `{A,B}` is the
unique illegal turn. The only seed turn in an edge image is `{B,c}`. Its
direction-map orbit consists of exactly thirteen turns:

`{c,B},{d,C},{a,D},{b,A},{c,C},{d,D},{a,A},{b,C},{c,D},{d,A},{a,C},{b,D},{c,A}`.

This set is direction-map closed and never contains `{A,B}`. Therefore all
iterates are reduced train-track iterates, and the unique illegal turn is never
taken by any positive power. The standard indivisible Nielsen-path lemma then
rules out periodic Nielsen paths.

The local Whitehead graph is connected. Removing the one nonperiodic direction
`B` leaves exactly the twelve positive-negative turns, so the stable Whitehead
graph is `K_{4,3}`.

## Full irreducibility and ageometricity

The criterion used here is Pfaff's Full Irreducibility Criterion: a PNP-free
train-track representative with Perron-Frobenius transition matrix and connected
local Whitehead graphs represents an ageometric fully irreducible outer
automorphism. All three hypotheses were established above. This replaces the
earlier wording that attributed the conclusion merely to irreducibility and
Whitehead connectivity; that wording omitted the essential no-periodic-Nielsen-
path hypothesis.

For a PNP-free fully irreducible rose representative, the ideal Whitehead graph
is the stable Whitehead graph. Thus `IW(phi)=K_{4,3}`. Its single component has
seven vertices, giving `i(phi)=1-7/2=-5/2`. Since `1-4=-3 < -5/2 < 0`, the
index is consistent with the ageometric case.

The positive directions have period four under `Df`, while `A,C,D` have period
three. Hence `Df^12` fixes every periodic direction. The rose vertex is fixed
and principal, and there are no PNPs, giving the stated rotationless power.

Finally, an ageometric fully irreducible is nongeometric; the standard
fully-irreducible dichotomy then implies atoroidality. Brinkmann's theorem
consequently gives a hyperbolic mapping torus.

## Originality context

Pfaff constructed and analyzed broad families of ideal Whitehead graphs and
proved the full-irreducibility criterion used above. The retrieved literature
does not supply this exact substitution or this `K_{4,3}` computation. The
contribution here is therefore a concrete explicit example and exact invariant
calculation, not a new general irreducibility theorem.

## Limitations

The repository verifier checks the finite substitution, direction, turn and
Whitehead-graph calculations. Its NumPy determinant/characteristic-polynomial
lines are numerical sanity checks; the exact determinant and characteristic
polynomial used above follow by direct integer expansion. The deductions from
the finite certificate to full irreducibility, rotationlessness and
atoroidality use standard train-track theorems.

## Reproducibility

Run `python3 artifacts/certify.py` from the record directory.

## References

- C. Pfaff, *Ideal Whitehead Graphs in Out(F_r) II: The Complete Graph in Each Rank*, especially Proposition 4.1 (Full Irreducibility Criterion).
- Bestvina-Handel, *Train tracks and automorphisms of free groups*.
- Gaboriau-Jaeger-Levitt-Lustig, index theory for automorphisms of free groups.
- Handel-Mosher and subsequent train-track literature for rotationless representatives and ideal Whitehead graphs.
- Brinkmann, hyperbolic mapping tori of free-group automorphisms.
