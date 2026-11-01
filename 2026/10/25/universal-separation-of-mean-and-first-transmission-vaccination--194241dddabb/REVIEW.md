# Independent mathematical audit

## correctness

PASS

Reconstructed the entire n>=2 and 0<p<1 proof. After deleting j, remaining lengths a=j-1,b=n-j, the random-seed mean is 1+2(F_p(a)+F_p(b))/(n-1), with F_p(k)=sum_{d=1}^{k-1}(k-d)p^d. Strictly increasing first differences sum_{d=1}^k p^d force balanced components. The non-singleton-cluster probability is [L_p(a)+L_p(b)]/(n-1), L_p(0)=L_p(1)=0 and L_p(k)=2p+(k-2)(2p-p^2) for k>=2. For n>=5, two nontrivial residual components have risk numerator larger by p^2 than removal at j=2 or n-1; endpoint removal larger by 2p-p^2. n=4 and n=2,3 cases directly checked, and all <=4-vertex trees are paths or the star with a uniquely dominating center. Thus all optimizers and the smallest-tree P5 boundary are correct. An independent distance-weight and vertex-degree checker (not packaged code) exactly checked all n=2..11 at p=1/5,1/2,4/5. Finite tests alone do not imply the all-n theorem.

## originality

PASS

Best-of-knowledge originality for the exact joint path optimizer classification and sharp smallest-tree boundary, not for the general observation that outbreak-size loss functions disagree. Primary Yuan et al. (2015) and Holme (2017) were inspected in accessible full text; they do not mathematically imply the specified center-versus-second-nearest-endpoints classification for independent-bond seed clusters. Published-result semantic searches found path/graph extremality for unrelated invariants, not this objective pair. This is a qualified priority assessment, not a proof that no older equivalent exists.

## value

PASS

The two loss criteria are independently motivated in primary vaccination literature. The result classifies the exact optimizer sets for an entire canonical infinite family of paths at every transmission probability, and identifies the sharp five-vertex minimum among all trees for disjoint optima. It quantifies an explicit tradeoff on P5 (extra mean p^2/2 for a p^2/4 decrease in onward-infection probability). This is a natural complete extremizer/boundary classification, not an arbitrary tiny instance or a claim of realistic optimal epidemiological policy. The required proof is elementary but solves the specifically stated motivated optimization problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
