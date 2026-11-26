# Independent mathematical audit

## correctness

PASS

Independent obstruction: let A be the original closure. If the altered process first adopts a vertex outside A, only w can be that vertex; for states inside A the original closure rules exclude untouched vertices, and v replaces the permanent seed a by at most one adopter. Also v must already have adopted before w, otherwise the extra neighbor only dilutes w’s fraction. Thus a and v belong to A. Stop before this first escape: v cannot have adopted with A={a,v}, since the a-edge is gone and no other available adopter could trigger it. Hence |A|≥3. Initial connectedness gives w positive degree, and w must have a neighbor outside A (otherwise it would adopt originally at θ<1). On at most five vertices, A therefore has exactly three vertices, and its complement is {w,t} with wt an edge. Let k be the number of w-neighbors in A originally. Necessarily k/(k+1)≤θ<(k+1)/(k+2); here all k original A-neighbors are retained and v is added. If k=0 then θ<1/2, so t cannot have any neighbor in A either (one or more would give at least 1/2 at the original stable state), contradicting connectedness. If k≥1 then θ≥1/2. But before escape v has at most one available adopter (the third member of A) and at least one nonadopter neighbor w, so the strict rule prevents its adoption. This proves even closure inclusion at orders ≤5. At six vertices 1 adopts before 0 in the altered tree, enabling 0 at fraction 1/2, then leaves 4 and 5. In the original tree vertex 0 has fraction 1/3 until it or its leaves adopt, so all three stay out on exactly the required interval, including its lower endpoint. Both graphs have five edges and are connected. Appending leaves at unchanged permanent seed 3 gives sizes n−3 and n. A separate exact finite replay agrees with the source counts and the witness.

## originality

PASS

The sharp connected-network order threshold for one specified deterministic edge move, under strict homogeneous fractional adoption, is the supported distinct finding. Promotion of adoption by rewiring and the existence of other tree witnesses are not by themselves credited as new. Neither the closely related indexed tree construction nor the inspected literature gives the lower-order obstruction in this model.

## value

PASS

This isolates the minimum number of vertices needed for an initially adverse single homophilic move to improve the eventual cascade, a question left open by large-network ensemble behavior. Tree-to-tree sharpness and a nonzero interval of strict thresholds show the gain is not a cyclic-graph or tie-breaking accident. The exact small-order obstruction is independently useful for testing purported mechanisms, not an arbitrary sample-size computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
